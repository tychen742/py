import ast
import contextlib
import io
import json
import sys


ALLOWED_CALLS = {
    "print": print,
    "int": int,
    "round": round,
    "ord": ord,
    "bin": bin,
    "hex": hex,
    "str": str,
    "float": float,
    "type": type,
    "bool": bool,
    "sum": sum,
    "len": len,
    "max": max,
    "min": min,
    "set": set,
    "sorted": sorted,
    "range": range,
    "enumerate": enumerate,
    "zip": zip,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "abs": abs,
    "iter": iter,
    "next": next,
    "isinstance": isinstance,
    "issubclass": issubclass,
    "super": super,
    "map": map,
    "filter": filter,
    "any": any,
    "all": all,
    "reversed": reversed,
    "frozenset": frozenset,
    "object": object,
    "staticmethod": staticmethod,
    "classmethod": classmethod,
    "property": property,
    "ValueError": ValueError,
    "TypeError": TypeError,
    "KeyError": KeyError,
    "IndexError": IndexError,
    "ZeroDivisionError": ZeroDivisionError,
    "AttributeError": AttributeError,
    "StopIteration": StopIteration,
    "NameError": NameError,
    "RuntimeError": RuntimeError,
    "Exception": Exception,
    # Compiler-synthesized calls: the `class` and `import` statements invoke
    # these internally via dedicated bytecode ops, never through a Name/Call
    # AST node in student source, so the dunder-prefix checks below (which
    # block any *explicit* reference to a `__`-prefixed identifier) still
    # prevent student code from grabbing these directly.
    "__import__": __import__,
    "__build_class__": __build_class__,
}

# Explicit-call dunder methods needed for idiomatic OOP/iterator code
# (e.g. `super().__init__(...)`, custom `__iter__`/`__next__` invocation).
# Deliberately excludes introspection/escape-prone dunders such as
# __class__, __bases__, __subclasses__, __globals__, __dict__, __code__,
# __getattribute__, __reduce__, __import__, etc.
SAFE_DUNDER_METHODS = {
    "__init__",
    "__str__",
    "__repr__",
    "__eq__",
    "__ne__",
    "__lt__",
    "__le__",
    "__gt__",
    "__ge__",
    "__len__",
    "__iter__",
    "__next__",
    "__contains__",
    "__hash__",
}

# NOTE: deliberately excludes str.format()/str.format_map() — their
# "{0.__class__}" field-access mini-language does attribute traversal at
# runtime via a string spec, invisible to the AST validator below, and is
# a known sandbox-escape primitive. Use f-strings instead (already
# supported via JoinedStr/FormattedValue, which DO compile to real
# Attribute AST nodes the validator can see).
ALLOWED_METHODS = {
    "append",
    "count",
    "get",
    "index",
    "items",
    "keys",
    "lower",
    "split",
    "strip",
    "upper",
    "values",
    "sort",
    "pop",
    "join",
    "replace",
    "extend",
    "insert",
    "setdefault",
    "popitem",
    "discard",
    "union",
    "intersection",
    "difference",
    "remove",
    "add",
    "update",
    "copy",
    "casefold",
    "startswith",
    "endswith",
    "isdigit",
    "isalpha",
    "isalnum",
    "istitle",
    "isupper",
    "islower",
    "isspace",
    "find",
    "rfind",
    "capitalize",
    "title",
    "zfill",
    "ljust",
    "rjust",
    "center",
    "rstrip",
    "lstrip",
    "splitlines",
    "partition",
    "rpartition",
    "swapcase",
    "match",
    "search",
    "findall",
    "finditer",
    "fullmatch",
    "sub",
    "subn",
    "group",
    "groups",
    "groupdict",
    "span",
    "start",
    "end",
}

# Root package names allowed in `import`/`from ... import ...` statements.
# All pure-computation stdlib modules: no filesystem, network, process,
# or introspection capability. os/sys/subprocess/socket/pathlib/requests/
# importlib/threading/multiprocessing are deliberately excluded.
ALLOWED_MODULES = {
    "math",
    "random",
    "string",
    "re",
    "itertools",
    "functools",
    "collections",
    "bisect",
    "dataclasses",
    "abc",
    "contextlib",
    "datetime",
    "time",
    "timeit",
    "json",
}

ALLOWED_NODES = (
    ast.Module,
    ast.Assign,
    ast.AnnAssign,
    ast.Expr,
    ast.Name,
    ast.Load,
    ast.Store,
    ast.Constant,
    ast.BinOp,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.FloorDiv,
    ast.Mod,
    ast.Pow,
    ast.UnaryOp,
    ast.UAdd,
    ast.USub,
    ast.Call,
    ast.keyword,
    ast.JoinedStr,
    ast.FormattedValue,
    ast.Attribute,
    ast.Compare,
    ast.Eq,
    ast.NotEq,
    ast.Lt,
    ast.LtE,
    ast.Gt,
    ast.GtE,
    ast.BoolOp,
    ast.And,
    ast.Or,
    ast.Not,
    ast.If,
    ast.IfExp,
    ast.For,
    ast.While,
    ast.AugAssign,
    ast.List,
    ast.Tuple,
    ast.Set,
    ast.Dict,
    ast.Starred,
    ast.Subscript,
    ast.Slice,
    ast.FunctionDef,
    ast.arguments,
    ast.arg,
    ast.Return,
    ast.Pass,
    ast.ListComp,
    ast.SetComp,
    ast.DictComp,
    ast.GeneratorExp,
    ast.comprehension,
    ast.Try,
    ast.ExceptHandler,
    ast.Raise,
    ast.Assert,
    ast.ClassDef,
    ast.Lambda,
    ast.Yield,
    ast.YieldFrom,
    ast.Import,
    ast.ImportFrom,
    ast.alias,
    ast.With,
    ast.withitem,
)


class LabCodeValidator(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        # Names bound by a vetted `import X [as Y]` statement. Attribute
        # calls on these (e.g. `math.sqrt(...)`) bypass the object-method
        # allowlist below, since the module itself was already restricted
        # to ALLOWED_MODULES at import time.
        self.imported_modules = set()

    def generic_visit(self, node):
        if not isinstance(node, ALLOWED_NODES):
            raise ValueError(f"{type(node).__name__} is not allowed in this lab.")
        super().generic_visit(node)

    def visit_Name(self, node):
        if node.id.startswith("__"):
            raise ValueError("Names beginning with __ are not allowed.")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if node.attr.startswith("__") and node.attr not in SAFE_DUNDER_METHODS:
            raise ValueError("Attributes beginning with __ are not allowed.")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id.startswith("__"):
                raise ValueError("Names beginning with __ are not allowed.")
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            base = node.func.value
            is_module_call = isinstance(base, ast.Name) and base.id in self.imported_modules
            if attr in SAFE_DUNDER_METHODS or is_module_call:
                pass
            elif attr not in ALLOWED_METHODS or attr.startswith("__"):
                raise ValueError("Only the allowed lab methods can be called.")
        else:
            raise ValueError("Only simple function and method calls are allowed.")
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias_node in node.names:
            root = alias_node.name.split(".")[0]
            if root not in ALLOWED_MODULES:
                raise ValueError(f"Importing '{alias_node.name}' is not allowed in this lab.")
            self.imported_modules.add(alias_node.asname or root)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.level != 0:
            raise ValueError("Relative imports are not allowed in this lab.")
        root = (node.module or "").split(".")[0]
        if root not in ALLOWED_MODULES:
            raise ValueError(f"Importing from '{node.module}' is not allowed in this lab.")
        for alias_node in node.names:
            if alias_node.name == "*":
                raise ValueError("Star imports are not allowed in this lab.")
        self.generic_visit(node)


def run_code(code):
    tree = ast.parse(code, mode="exec")
    LabCodeValidator().visit(tree)
    compiled = compile(tree, "<student-code>", "exec")
    stdout = io.StringIO()
    # __name__ is a plain string constant (no capability), needed because
    # class statements read the caller's module __name__ to set __module__.
    safe_globals = {"__builtins__": ALLOWED_CALLS, "__name__": "student_lab"}
    with contextlib.redirect_stdout(stdout):
        exec(compiled, safe_globals)
    return stdout.getvalue()


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
        code = str(payload.get("code", ""))
        output = run_code(code)
        print(json.dumps({"ok": True, "stdout": output, "stderr": "", "error": None}))
    except Exception as exc:
        print(json.dumps({"ok": False, "stdout": "", "stderr": "", "error": str(exc)}))


if __name__ == "__main__":
    main()

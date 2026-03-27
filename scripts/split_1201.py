"""
Split chapters/12-oop/1201-oop-design.ipynb at cell 174.
Cells 0-173  → stay in 1201-oop-design.ipynb   (Classes/Functions + Design-First + Operators)
Cells 174-end → new  1201b-oop-objects.ipynb     (Point, Line, Rectangle applied examples)
"""
import json, copy, uuid, pathlib

src = pathlib.Path("chapters/12-oop/1201-oop-design.ipynb")
dst = pathlib.Path("chapters/12-oop/1201b-oop-objects.ipynb")

SPLIT = 174  # first cell of ## Classes and Objects

with src.open() as f:
    nb = json.load(f)

cells = nb["cells"]
keep  = cells[:SPLIT]
move  = cells[SPLIT:]

# --- Trim 1201: add a closing summary cell at the end ---
summary_cell = {
    "cell_type": "markdown",
    "id": str(uuid.uuid4())[:8],
    "metadata": {},
    "source": [
        "## Summary\n\n",
        "In this notebook we covered:\n\n",
        "- **Programmer-defined types**: creating classes and working with object attributes, mutation, and copying\n",
        "- **Pure functions vs. modifiers**: designing methods that avoid surprising side effects\n",
        "- **Classes and methods**: `__init__`, `__str__`, `__repr__`, `@staticmethod`, `@classmethod`, `@property`\n",
        "- **Operator overloading**: defining `__add__` and related methods so objects support Python operators\n",
        "- **Design-first development**: prototype-and-patch, then refactor to clean class design\n\n",
        "Next: **OOP Applied** — working with Point, Line, and Rectangle classes in a geometry library."
    ]
}
keep.append(summary_cell)

nb_keep = copy.deepcopy(nb)
nb_keep["cells"] = keep
with src.open("w") as f:
    json.dump(nb_keep, f, indent=1)
print(f"1201-oop-design.ipynb: {len(keep)} cells")

# --- Build 1201b: prepend H1 title cell ---
title_cell = {
    "cell_type": "markdown",
    "id": str(uuid.uuid4())[:8],
    "metadata": {},
    "source": ["# OOP Applied: Point, Line, and Rectangle\n\n",
               "This notebook continues Chapter 12 by working through a practical geometry\n",
               "library. You will apply the class design skills from the previous notebook\n",
               "to build and manipulate `Point`, `Line`, and `Rectangle` objects.\n\n",
               "Topics covered:\n",
               "- Creating and printing geometric objects\n",
               "- Equivalence vs. identity (`==` vs. `is`)\n",
               "- Mutating objects; deep vs. shallow copy\n",
               "- Operator overloading in an applied context"]
}
move.insert(0, title_cell)
# Replace the inherited ## heading with ### to avoid duplicate H2 under new H1
first_heading_cell = move[1]  # original cell 174 = "## Classes and Objects"
src_lines = first_heading_cell["source"]
if isinstance(src_lines, list):
    src_lines[0] = src_lines[0].replace("## Classes and Objects", "## Classes and Objects", 1)
    # Keep as ## — it's a valid H2 under the new H1

nb_move = copy.deepcopy(nb)
nb_move["cells"] = move
nb_move["metadata"]["kernelspec"] = nb["metadata"].get("kernelspec", {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
})
with dst.open("w") as f:
    json.dump(nb_move, f, indent=1)
print(f"1201b-oop-objects.ipynb: {len(move)} cells")

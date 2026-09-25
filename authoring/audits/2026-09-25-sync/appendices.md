---
orphan: true
---

## Sync Audit — Appendices (Course Tooling, Jupyter Setup, Modules and Packaging)

Scope: `chapters/appendices/{ORGANIZATION,MATERIALS}.md` (0101-tooling + jupyter/ unit), `chapters/appendices/packaging/{ORGANIZATION,MATERIALS}.md` (0500–0504), the notebooks, `_toc.yml` lines 237–256, and `materials/appendices/packaging/`. Audited as on disk, 2026-09-25. Items under "Planned Additions" (0102-git, ruff, argparse/sys.argv, pyproject/uv, moving 0501 to Ch08, trimming 0504) are known and not flagged as missing.

### Planning docs ↔ chapter

**Front matter and file inventory**

✗ Front matter: none of the four docs starts with MyST `orphan: true`. All four open directly with an H1 (`# Appendices Organization`, `# Appendices Materials`, `# Appendix Organization (Modules, Files, and Tooling)`, `# Appendix Materials (Modules, Files, and Tooling)`). Only Ch08's docs have it so far, so this gap exists across the whole book. `materials/` is excluded in `_config.yml`, but `chapters/appendices/**/*.md` is not, so Sphinx will warn that these docs are not in any toctree.

✓ Notebook inventory: every notebook named in the docs exists (0101, jupyter/0200–0204, packaging/0500–0504). Every notebook on disk is named in the docs. `_toc.yml` order (0101, then 0200 plus 0201–0204, then 0500 plus 0501–0504) matches both delivery orders.

✗ Unit title disagrees in five places. The same unit is called:
- `Modules and Packaging` in `_toc.yml` line 251
- `Tooling` in the 0500 H1 (cell 0)
- `Modules, Files, and Tooling` in the packaging ORGANIZATION.md and MATERIALS.md H1s
- `Modules, files, and packaging` in appendices ORGANIZATION.md line 16

Separately, 0504's H1 is `Coding Patterns and Idioms`, while the docs call it "Coding tooling patterns". "Tooling" is also the title of the separate 0101 page (`Course Tooling`), so readers see two different "Tooling" entry points. The TOC and folder name (`packaging`) look current; the doc H1s and the 0500 H1 look stale.

**Section sequence and coverage: 0101 and jupyter/ (appendices ORGANIZATION.md / MATERIALS.md)**

✗ 0101-tooling description is wrong. Both docs call it "Development tools and environment setup overview" (ORG line 9, MAT lines 7 and 42). The notebook's `##` headings are Editing Tools (cell 2), The File System (cell 5), Command Line Basics (cell 13, with Pathname and Special Characters, Essential Commands, and Creating Directories and Files), and The Python Shell (cell 21). It does not cover environment setup; that lives in jupyter/0201–0202. The doc is stale.

✗ jupyter/0204-jupyter-bonus description is wrong. The docs say "Advanced Jupyter tips, extensions, and productivity tricks" (ORG line 15, MAT lines 12 and 47). The notebook has no `##` headings, and its only content is creating the shell aliases `pyd`, `venv`, and `jn` on Windows (PowerShell profile) and macOS (`.bashrc`/`.zshrc`) (cells 1–2). There are no extensions and no Jupyter tips. The doc is stale, or it describes content that was never written.

✗ jupyter/0200 and 0201 are described inaccurately.
- 0200: ORG line 11 says "Introduction to Jupyter notebooks and interactive computing". Cell 0 is actually a setup roadmap: a table comparing Jupyter, VS Code, Anaconda, and Colab, plus a list of install steps.
- 0201: ORG line 12 says "installation guides for all platforms", and MATERIALS "Must-Have" line 17 lists Windows, macOS, and Linux. The notebook's tab-sets cover only Windows and macOS (cells 5–8), with no Linux tab.

✗ No topic-level sequence exists for 0101 or jupyter/. The appendices ORGANIZATION.md gives one line per notebook and no section list. As a result, none of the taught `##` topics can be checked against the docs, and all of them are effectively unlisted. Examples:
- 0101: Python shell / REPL, pathname characters, and the essential command table
- 0201: Check Existing Python, Install Python, Choose Python Version, and `PATH` editing
- 0202: project directory, create, activate, and deactivate `.venv`
- 0203: Code Cells, Markdown Cells, Keyboard Shortcuts, kernel restart/interrupt, and Key Takeaways

✗ Practice and assets are listed but do not exist. Appendices MATERIALS.md "Practice and Assessment" (lines 24–26) lists "Checkpoint exercises for environment verification". 0101 and jupyter/0200–0204 have no exercises (no `thebe-interactive` cells). "Reusable Assets" (lines 30–33) lists setup scripts and Jupyter configuration examples, but no such files exist under `materials/appendices/`. Either mark them as to-do or remove them.

**Section sequence and coverage: packaging/ (0500–0504)**

✗ 0500 section numbers are stale. The overview table and the "How to use" bullets in cell 0 refer to "5.1 — Files", "5.2 — Modules", "5.3 — Packaging", "5.4 — Coding Tooling", "Browse 5.1–5.3", and "Treat 5.4 as a recipe book". Cell 1 says "In 5.2 you will write your own module. In 5.3 …". These are the numbers from the old Chapter 5. `_toc.yml` now puts the unit under "Appendices" with `restart_numbering: true`, where it is the third entry, and Chapter 5 is now `05-testing`. The notebook is stale.

✗ 0500 headings are not real `##` headings, and the hierarchy topic does not match.
- Cell 1 uses raw HTML `<h2>What is a Module?</h2>` and `<h2>Importing Patterns</h2>`, so 0500 has no `##` headings for the page TOC or the sequence check.
- ORG line 18 lists a "module/package/library hierarchy". Cell 1 teaches function → module → package. "Library" is introduced only in 0503 cell 3.
- As the unit landing page, 0500 also teaches import syntax, which the book-authoring landing-page rule reserves for content notebooks. If this is intentional for an appendix, the doc should say so.

✗ 0501 has sections that the docs never mention.
- `## Download Files` (cell 3) is an empty heading.
- `## Custom Code` (cells 4–6) teaches the `shared` helper package: the `download()` helper, the `__init__.py` package marker, and the project-root `sys.path` snippet.

Neither topic appears in ORG line 20, ORG line 50, or MAT line 29. The notebook order is Download Files → Custom Code → `with` → `Path()`. The docs list only "read/write text files; `Path()`", so they are out of order and incomplete.

✗ 0501 "Reading/writing text files" is only partly taught. Both docs list it as the page's core topic. The text in cell 7 explains only opening and closing, and `with` as a context manager.
- Cell 8 uses write mode `open(..., 'w')`, `f.write()`, and `f.read()`, but no markdown explains file modes (`'r'`, `'w'`, `'a'`), `write`, `read`, or reading line by line. This is house rule (b): the example uses syntax the text has not taught.
- The `Path` methods in cell 12 (`read_text`, `write_text`, `unlink`, `iterdir`, `glob`, `rglob`, `exists`, `is_file`) appear only as code comments. Cell 9 text says only "import `Path()`; build the path".

✗ 0501 `download()` example contradicts its own text (house rule (b)).
- Cell 5 shows `def download(url):`, with one parameter.
- Cell 14 calls `download('https://…/words.txt', words_path)`, with two arguments. The two-argument form, `download(url, dest=None)` in `shared/download.py`, is never shown.
- In this notebook, cell 1 binds `download` to the module (`from shared import … download …`), not to the function. If `words.txt` is missing, cell 14 would raise `TypeError: 'module' object is not callable`.

✗ 0501 has a stale cross-reference. The note in cell 7 says "Ch13 explains how to build your own context managers." Context managers are taught in Ch10: `chapters/10-functional/1002-func-practice.ipynb`, cell 10, `## Context Managers`, using `contextlib.contextmanager`. Ch13 (abstract data structures) has no context-manager content. The notebook is stale.

✗ The `__main__` guard is listed but not taught. The docs list it in six places:
- ORG line 22 (sequence)
- ORG line 44 (Duplication rules: "`__main__` guard: **0502 only**")
- ORG line 51 (File Roles)
- MAT line 33 (content target)
- MAT line 71 (delivery order)
- MAT line 49 (lab task "add __main__ guard to a script")

0502 contains no `__main__` or `__name__` anywhere. Its headings are What Is a Module? (cell 3), Create and Import Your Own Module (cell 5), Module Design for Projects (cell 9), and Summary (cell 11). A repo-wide search finds the `if __name__ == "__main__":` idiom taught nowhere in the book. The only hits are the `patch("__main__.get_price")` targets in `05-testing/0502-unit-testing.ipynb`. The guard is not one of the Planned Additions; the argparse item only says "alongside the existing `__main__` guard", which assumes it is already there. Either the notebook lost this section or it was never written. Because the Duplication rule forbids teaching it elsewhere, the gap is book-wide.

✗ 0502 teaches topics the docs don't list, and its exercise depends on untaught mechanics.
- `## Module Design for Projects` (cells 9–10: `main.py` plus utility-module split, keeping functions small) is not in either doc.
- Cell 6 makes a module importable using `Path.mkdir(parents=True, exist_ok=True)`, `Path.write_text`, `Path.resolve()`, and `sys.path.insert(0, …)`. None of this is explained in markdown; cell 5 says only "A custom module is just a `.py` file".
- The exercise "Build a Tax Module" (cell 7, solution cell 8) requires the same `sys.path` and module-file mechanics. This is house rule (b): the text never teaches the module search path (`sys.path`) or why the folder must be on it.

✗ 0503: the two docs disagree, and some taught topics are unlisted.
- ORG lines 24 and 52 list "package structure; `__init__.py`; `pip`; `requirements.txt`; virtual environments".
- MAT lines 37 and 72 list only "Package structure; __init__.py; pip install basics", omitting `requirements.txt` and virtual environments. MATERIALS.md is stale.
- Taught but not listed in either doc: the module/package/library table (cell 3), `importlib.reload` (cell 7), running pip from Python with `subprocess.run([sys.executable, '-m', 'pip', …])` (cells 11–12), and checking the active interpreter with `sys.executable`/`sys.version` (cell 16).

✗ 0503 exercises are not tagged.
- "Exercise: Extend the Package" (cell 8) and "Exercise: pip show" (cell 17) have no `thebe-interactive` tag.
- Their solution cells 9 and 18 have no `hide-input` tag, so the solutions render in full right after the prompts.
- This violates the ORG Build/Quality checklist (line 70) and the house exercise format.

✗ 0503 "Exercise: pip show" relies on untaught syntax (house rule (b)).
- Cell 10's text says "In a notebook you can prefix any shell command with `!` to run it", but no `!` example follows. Cells 11–12 use `subprocess.run(..., capture_output=True, text=True)` with no explanation.
- The exercise (cell 17) explicitly requires subprocess, which the text never teaches.
- The exercise also suggests `'pathlib'` as an installed package. `pathlib` is standard library, so `pip show pathlib` finds nothing.

✗ Virtual environments are taught twice with no ownership rule. 0503 `## Virtual Environments` (cell 15) repeats `jupyter/0202-virtual-environment.ipynb` (create, activate, and deactivate `.venv`). The packaging ORG "Duplication rules" (lines 41–45) cover `with` and `__main__` but not venv. The appendices ORGANIZATION.md does not cross-link the two units. Pick one owner and have the other link to it.

✗ 0504 target disagrees across the docs and with the notebook.
- ORG lines 26 and 53 list seven topics in notebook order: comprehensions, lambda, docstrings/`help()`, type hints, `enumerate`/`zip`, `try`/`except`, and f-string formatting. This matches the `##` headings in cells 3, 10, 12, 14, 16, and 18.
- MAT line 41 says only "Comprehensions with lambdas; coding tooling patterns; try-exception".
- MAT line 73 (delivery order) drops try/except as well, so it contradicts line 41.
- Taught but unlisted: `map()`/`filter()`/`sorted(key=…)` with lambda (cells 5–7), `__doc__` (cell 11), `typing.Optional`/`Union` (cell 12), and `else`/`finally` clauses (cell 16).
- Note on Planned Additions: the 0504 item (ORG line 38) lists the re-taught topics with their home sections but omits docstrings. Docstrings are also taught in 4.2 (`04-functions/0402-function-design.ipynb`, `## Docstrings`).

**Exercise lists**

✗ Neither doc lists any exercises. The notebooks contain four:
- 0502 "Build a Tax Module" (cell 7)
- 0503 "Extend the Package" (cell 8)
- 0503 "pip show" (cell 17)
- 0504 "Comprehension + Lambda" (cell 8)

0500 and 0501 have none. That contradicts the ORG checklist line 68, "at least one checkpoint exercise per major section", and leaves 0501's file read/write topic without practice. The docs need an exercise list.

✗ Packaging MATERIALS.md "Practice and Assessment Pack" (lines 43–55) and "Must-Have" (line 13) describe things that don't exist: in-class polls, "predict the output" questions, lab tasks, a homework, and a slide deck. The appendix has no `assignments/` folder and no slide deck. Of the three lab tasks, only "Build a tax module" exists, as the 0502 exercise. "Write/read a text file" has no exercise, and "add __main__ guard" has no teaching. This looks like an unedited chapter template.

**Material files**

✓ `materials/appendices/packaging/` exists. Its runnable modules are all written and read by the notebooks at that path:
- `my_math_tools.py` (0502 cell 6)
- `pricing_tools.py` (0502 cell 8)
- `my_package/` with `__init__.py`, `math_tools.py`, `text_tools.py`, `list_tools.py` (0503 cells 5 and 9)
- `requirements_demo.txt` (0503 cell 14)

`__pycache__/` is git-ignored.

✗ `demo.txt` is misattributed. Appendices MATERIALS.md line 38 says `demo.txt` is used only by the archived `materials/_archived/appendix-tooling-old/0501-files_OLD.ipynb`. That notebook contains no "demo" string, and no notebook in `chapters/` references `demo.txt`; the only matches are `requirements_demo.txt`. The file is orphaned.

✗ `text_file.txt` is unlisted and unused. `materials/appendices/packaging/text_file.txt` is not named in either doc, and nothing reads it. 0501 cell 8 writes to and reads from `../../../data/text_file.txt` instead. This is a leftover from the move; either point 0501 at the materials copy (matching the packaging ORG line 58 claim that text files live in `materials/appendices/packaging/`) or delete it and list `data/text_file.txt`.

✓ The other archived-only files are correctly attributed: `anagram_map`, `camel-spotting-book.txt`, `config.yaml`, `notes.txt`, and `photo_info/` are referenced only by the archived 0501-files_OLD notebook.

**Stale references**

✓ There are no remaining `05-tooling` or `05-modules` paths in any notebook, doc, `.yml`, or `.py` under `chapters/` or `materials/`. The only hits are the intentional archive pointer in MATERIALS.md line 38.

✗ There is a numbering collision in Planned Additions (a reference problem, not a coverage flag). Packaging ORG line 32 plans to move 0501 into "Chapter 8 (`0802-files.ipynb`)", but `chapters/08-strings/0802-regex.ipynb` already occupies 0802 in `_toc.yml` line 119. The target number needs renumbering or a different slot.

**Learning objectives**

✓ Not applicable. Neither ORGANIZATION.md has a learning-objectives section. The per-notebook "Learning Goals" in 0502 (cell 2) and 0503 (cell 2) are consistent with their own headings, except that 0502's goals also omit the `__main__` guard.

**Other observations (outside check 1, found while verifying)**

- The 0201 figures in cell 8 point to missing files. `figures/PATH_Windows_environment_variables.png` and `figures/PATH_Windows_Edit_environment_variables.png` do not exist; the files on disk are `PATH_Windows_environment-variables.png` and `PATH_Windows_Edit-environment-variables.png` (hyphens). Both images will render broken.
- In 0101 cell 20, the macOS tab runs `nano text_file.txt` while the prose and the following `ls` use `test_file.txt`. The same tab uses the Windows-style `cat .\test_file.txt` inside a bash block.
- In the 0504 cell 18 format table, the `{x:,.2f}` row's example is `f"{1234567.8:.2f}"` (no comma), which would not produce the listed `1,234,567.80`.
- 0200 cell 0 says "follow the four steps below" and then lists five.

### Slide deck ↔ chapter
Not applicable: the appendices have no slide deck.

### Preview ↔ chapter
Not applicable: the appendices have no preview assignment.

### Homework ↔ chapter
Not applicable: the appendices have no homework.

### Lab ↔ chapter
Not applicable: the appendices have no lab.

### Glossary ↔ content
Not applicable: the appendices have no landing-page glossary.

### Summary
Sync issues: 23
  - All four planning docs lack `orphan: true` front matter
  - The unit title disagrees across `_toc.yml`, the 0500 H1, both packaging docs, and the appendices ORG (0504 H1 also differs)
  - 0101 is described as "environment setup"; it actually covers editors, file system, CLI, and the Python shell
  - 0204 is described as "advanced tips/extensions"; it contains only shell aliases
  - 0200 and 0201 descriptions are inaccurate (0201 has no Linux coverage)
  - No topic-level sequence exists for 0101 or jupyter/0200–0204
  - Appendices MATERIALS.md lists checkpoint exercises and setup/config assets that don't exist
  - 0500 uses stale "5.1–5.4" numbering from the old Chapter 5
  - 0500 uses HTML `<h2>` instead of `##`; its "library" hierarchy is taught in 0503, not 0500
  - 0501 `## Download Files` / `## Custom Code` (shared helpers) are not in the docs, and the section order differs
  - 0501 read/write is only partly taught: `'w'` mode, `write`/`read`, and `Path` I/O appear only in code
  - 0501 `download()` is shown with one parameter but called with two, and the name is bound to the module
  - 0501 says context managers are taught in "Ch13"; they are in Ch10 (1002)
  - The `__main__` guard is listed in both docs (and in a lab task) but is taught nowhere in the book
  - 0502 "Module Design for Projects" is unlisted; `sys.path` mechanics are used by the example and exercise but not taught
  - 0503 MATERIALS target omits `requirements.txt` and venv; `importlib`, `subprocess`, and `sys.executable` are unlisted
  - 0503 exercises and solutions are missing the `thebe-interactive` and `hide-input` tags
  - 0503 "pip show" exercise requires untaught `subprocess`; the `!` prefix is promised but never shown; it suggests `pathlib`
  - Virtual environments are taught in both 0503 and jupyter/0202 with no duplication rule
  - 0504 target disagrees between ORG and MAT (and within MAT); map/filter/sorted, typing, and else/finally are unlisted
  - Neither doc lists the 4 exercises; 0501 has none despite the checklist
  - Packaging MATERIALS.md lists labs, homework, polls, and a slide deck that don't exist
  - `demo.txt` is misattributed to the archived notebook, and `text_file.txt` is unlisted and unused

### Top fixes
1. **Resolve the `__main__` guard.** Add a `## Running a Module as a Script: the __main__ Guard` section to 0502 (Duplication rules make it the only home), or remove it from ORG lines 22, 44, 51 and MAT lines 33, 49, 71. It is currently taught nowhere in the book.
2. **Rewrite the appendices ORGANIZATION.md and MATERIALS.md descriptions of 0101, 0200, 0201, and 0204** to match the notebooks, and add a topic-level section sequence for each notebook. The current one-liners describe content that isn't there (environment setup in 0101, extensions and tips in 0204, Linux in 0201).
3. **Fix 0501's teaching gaps.**
   - Add markdown that teaches file modes and `read`/`write`, which today appear only in code.
   - Document or remove the `## Download Files` and `## Custom Code` sections, and fix the one-versus-two-argument `download()` mismatch and the module/function name clash (cells 1, 5, 14).
   - Change the "Ch13" pointer to Ch10 (`1002-func-practice`).
4. **Fix the 0503 exercises.**
   - Tag cells 8 and 17 `thebe-interactive` and cells 9 and 18 `hide-input`.
   - Either teach `subprocess.run` (and show the promised `!pip` form) in cell 10's text, or rewrite the "pip show" exercise so it doesn't need it, and replace the `pathlib` suggestion.
5. **Sync the packaging docs.**
   - Align MATERIALS.md with ORGANIZATION.md on the 0503 and 0504 targets and delivery order, and add an exercise list.
   - Replace the template "Practice and Assessment Pack" and slide-deck items.
   - Unify the unit title with `_toc.yml` ("Modules and Packaging") and 0500's H1; renumber 0500's "5.x" references.
   - Correct the `demo.txt` and `text_file.txt` material-file entries.
   - Add `orphan: true` front matter to all four docs.

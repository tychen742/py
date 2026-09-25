# Appendices Organization

This section contains practical setup and reference materials for students throughout the course.

## Content Structure

The appendices are organized into three units:

- `0101-tooling.ipynb` — Development tools and environment setup overview
- `jupyter/` — Jupyter and Python setup
  - `0200-intro-jupyter.ipynb` — Introduction to Jupyter notebooks and interactive computing
  - `0201-python-installation.ipynb` — Step-by-step Python installation guides for all platforms
  - `0202-virtual-environment.ipynb` — Virtual environment setup and management
  - `0203-the-notebook.ipynb` — Jupyter notebook features, workflows, and best practices
  - `0204-jupyter-bonus.ipynb` — Advanced Jupyter tips, extensions, and productivity tricks
- `packaging/` — Modules, files, and packaging (`0500`–`0504`); has its own `ORGANIZATION.md` and `MATERIALS.md`

## Planned Additions

Topics from the 2026-09-25 coverage review. Status: planned, not yet written. When a topic is written, move it into the content structure above and delete it here.

- **New page `0102-git.ipynb`**: git and GitHub basics: repositories, `git add`/`git commit`, reading `git status` and `git log`, branches, `.gitignore`, and pushing to GitHub. Add it to `_toc.yml` after `0101-tooling` when written.
  *Why:* industry practice; not covered anywhere in the book. It gets its own page because it is a whole workflow that students return to throughout the course.
- **`0101-tooling.ipynb`**: linting and formatting with `ruff`, and the PEP 8 style it enforces.
  *Why:* industry practice; PEP 8 is mentioned only in passing.
- Packaging-unit additions are listed in `packaging/ORGANIZATION.md`.

## File Roles

- Setup notebooks (`0101-tooling.ipynb`, `jupyter/0200`–`0204`): Provide students with working development environments
- `packaging/`: Modules, file I/O, packaging, and coding idioms reference

## Scope

The appendices provide foundational setup guidance and reference materials that students access throughout the course. These are not chapter content but rather enabling materials for working with Python and Jupyter.

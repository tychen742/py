#!/usr/bin/env bash
set -euo pipefail

build_dir="_build/html"
required_page="$build_dir/chapters/12-oop/1200-intro-oop.html"

if [[ ! -f "$required_page" ]]; then
  echo "Build output is incomplete: missing $required_page"
  echo "Run: .venv/bin/jupyter-book build . --builder html"
  exit 1
fi

# Copy standalone HTML assets into the built site without deleting normal book pages.
rsync -aL _html_extra/ "$build_dir/"

rsync -avz --delete "$build_dir/" tychen@thinkpy.org:/var/www/py/

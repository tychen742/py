#!/usr/bin/env bash

printf '\n\n########## start syncing ##########\n'

set -euo pipefail
trap 'echo "sync failed at line $LINENO: $BASH_COMMAND"' ERR

build_dir="_build/html"

if [[ ! -f "$build_dir/index.html" || ! -f "$build_dir/searchindex.js" ]]; then
  echo "Build output is incomplete. Run: jbb"
  exit 1
fi

# Copy standalone HTML assets into the built site without deleting normal book pages.
echo "Copying extra HTML assets..."
rsync -aL _html_extra/ "$build_dir/"

echo "Uploading built site..."
rsync -avz --delete "$build_dir/" tychen@thinkpy.org:/var/www/py/
printf '########## done syncing ##########\n'

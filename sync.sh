#!/usr/bin/env bash
set -euo pipefail

rsync -aL --delete _html_extra/ _build/html/
rsync -avz --delete _build/html/ tychen@thinkpy.org:/var/www/py/

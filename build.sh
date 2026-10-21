#!/usr/bin/env bash
# Usage: ./build.sh <batch.json ...>  (or --all). Full pipeline: merge the named research batches -> validate -> database/CSV/register -> PDF catalogue.
set -euo pipefail
cd "$(dirname "$0")"
python3 tools/merge.py "$@"
python3 tools/validate.py || { echo "Validation errors - fix data/ before publishing"; exit 1; }
python3 tools/build_db.py
python3 tools/build_pdf.py

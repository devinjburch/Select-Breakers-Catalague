#!/usr/bin/env bash
# Full pipeline: merge new research batches -> validate -> database/CSV/register -> PDF catalogue.
set -euo pipefail
cd "$(dirname "$0")"
python3 tools/merge.py
python3 tools/validate.py || { echo "Validation errors - fix data/ before publishing"; exit 1; }
python3 tools/build_db.py
python3 tools/build_pdf.py

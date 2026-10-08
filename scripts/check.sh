#!/usr/bin/env bash
# Check both the public root and a nested preview without touching preview files.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -B -m unittest discover -s scripts -p "test_*.py"
HUGO_BIN="${HUGO_BIN:-hugo}"
check_dir="$(mktemp -d "${TMPDIR:-/tmp}/rey-blog-check.XXXXXX")"
for route in production preview; do
  if [[ "$route" == production ]]; then
    base_url="https://blog.reywilliams.com/"
  else
    base_url="https://preview.example.test/preview/blog/"
  fi
  "$HUGO_BIN" --gc --minify --destination "$check_dir/$route" --baseURL "$base_url"
  python3 scripts/check-links.py --directory "$check_dir/$route" --base-url "$base_url"
done
printf 'Checked build artifacts: %s\n' "$check_dir"

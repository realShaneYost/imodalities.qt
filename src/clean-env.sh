#!/usr/bin/env bash
# Always stop if cmd fails and only run from script's dir
set -e
cd "$(dirname "$0")"

if [[ "$VIRTUAL_ENV" != "" ]]; then
  echo "⚠️ Subshell limitation, <deactivate> on complete!"
fi

if [[ -d "venv" ]]; then
  echo "✅ Removing venv/..."
  rm -rf venv
fi

echo "✅ Removing build artifacts..."
rm -rf build/ dist/ *.egg-info

echo "✅ Removing __pycache__ and *.pyc files..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.py[co]" -delete 2>/dev/null || true

echo "🧩 Recreate via..."
echo "   python3 -m venv venv"
echo "   source venv/bin/activate"
echo "   pip install -e ."


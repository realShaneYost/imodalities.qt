#!/usr/bin/env bash
# Always stop if cmd fails and only run from script's dir
set -e
cd "$(dirname "$0")"

if [[ -d "venv" ]]; then
  echo "⚠️ Existing virtual environment detected at ./venv"
  echo "❌ Aborted."
  exit 0
fi

echo "✅ Creating virtual environment..."
python3 -m venv venv

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "✅ Upgrading pip..."
pip install --upgrade pip

echo "✅ Installing modaldemo (editable mode)..."
pip install -e .

echo "✅ Deactivating environment..."
deactivate

echo ""
echo "🧩 Environment ready! Run via..."
echo "   <source venv/bin/activate>"
echo "   <python -m modaldemo.app> or <modaldemo>"


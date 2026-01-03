#!/usr/bin/env bash
set -e

echo "🔧 Setting up environment..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Setup complete"

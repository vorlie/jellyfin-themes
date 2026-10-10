#!/usr/bin/env bash
set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="${1:-$SCRIPT_DIR/..}"

python3 "$SCRIPT_DIR/start.py" "$TARGET_DIR"

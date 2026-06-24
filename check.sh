#!/bin/bash
# pre_push_check wrapper —— 自动检测项目路径和用户名，无需手动设环境变量
# 用法: ./check.sh [--quiet | --list]
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
export PRE_PUSH_PATH_PREFIX="$SCRIPT_DIR"
export PRE_PUSH_USERNAME="${USERNAME:-}"
export PYTHONIOENCODING=utf-8
python "$SCRIPT_DIR/pre_push_check.py" "$@"

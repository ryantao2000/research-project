#!/usr/bin/env bash
# 建立（或重建）lab的uv环境，并注册Jupyter内核。
#
#   bash lab/setup_env.sh            # 按 requirements.lock 精确安装
#   bash lab/setup_env.sh --relock   # 改了 requirements.txt 后，先重新生成锁文件再安装
#
# 环境在 lab/.venv（不进git）。任何机器只要有uv，运行本脚本即可得到同样版本的包。
set -euo pipefail

PYTHON_VERSION="3.12"
KERNEL_NAME="<kernel>"                 # 内核名：小写、无空格
KERNEL_DISPLAY="<项目名> (lab)"

LAB="$(cd "$(dirname "$0")" && pwd)"
cd "$LAB"

if [[ "${1:-}" == "--relock" || ! -f requirements.lock ]]; then
  uv pip compile requirements.txt --universal --python-version "$PYTHON_VERSION" -o requirements.lock
fi

uv venv .venv --python "$PYTHON_VERSION" --allow-existing
uv pip sync --python .venv/bin/python requirements.lock

# 本仓库的方法包也装进同一环境（可编辑安装）
if [[ -f ../code/pyproject.toml ]]; then
  uv pip install --python .venv/bin/python -e ../code
fi

.venv/bin/python -m ipykernel install --user --name "$KERNEL_NAME" --display-name "$KERNEL_DISPLAY"
echo "完成：在Jupyter或VS Code里选择内核 “$KERNEL_DISPLAY”。"

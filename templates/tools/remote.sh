#!/usr/bin/env bash
# 服务器部署与回传范例：按OPS中的服务器卡片修改REMOTE_ROOT等设置。
#   tools/remote.sh deploy <ssh别名> <NN_slug>   把已提交的代码与本计划执行区推到服务器
#   tools/remote.sh pull   <ssh别名> <NN_slug>   把本计划的run取回本机
# 只部署已提交的代码：有未提交改动时拒绝部署，并在服务器写入DEPLOYED_COMMIT。
set -euo pipefail

cmd=${1:?用法: remote.sh deploy|pull <ssh别名> <NN_slug>}
host=${2:?缺少ssh别名}
plan=${3:?缺少计划目录名，如 19_shared-world-cache}
REMOTE_ROOT=${REMOTE_ROOT:-"~/$(basename "$(git rev-parse --show-toplevel)")"}

cd "$(git rev-parse --show-toplevel)"
[ -d "work/$plan" ] || { echo "找不到 work/$plan" >&2; exit 1; }

case "$cmd" in
  deploy)
    paths=(code pyproject.toml uv.lock "work/$plan")
    if [ -n "$(git status --porcelain -- "${paths[@]}")" ]; then
      echo "以下文件有未提交的改动，请先提交再部署：" >&2
      git status --short -- "${paths[@]}" >&2
      exit 1
    fi
    commit=$(git rev-parse --short HEAD)
    ssh "$host" "mkdir -p $REMOTE_ROOT"
    rsync -azR --delete --exclude 'runs/' --exclude '__pycache__/' \
      "${paths[@]}" "$host:$REMOTE_ROOT/"
    ssh "$host" "echo $commit > $REMOTE_ROOT/DEPLOYED_COMMIT"
    echo "已部署 $commit → $host:$REMOTE_ROOT"
    ;;
  pull)
    mkdir -p "work/$plan/runs"
    rsync -az --stats "$host:$REMOTE_ROOT/work/$plan/runs/" "work/$plan/runs/"
    echo "已取回 $host:$REMOTE_ROOT/work/$plan/runs/ → work/$plan/runs/"
    ;;
  *)
    echo "未知命令: $cmd（可用 deploy / pull）" >&2; exit 1 ;;
esac

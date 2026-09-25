# OPS · 服务器与环境手册

<!-- 只写“现在怎么用”，信息变了就直接覆盖。每台机器一张卡片；探查过程、故障经过写进对应work/NN_slug/log.md，
     不写在这里。目标3–5KB。不记录密码与密钥。 -->

- **最近更新**：YYYY-MM-DD

## 本机

- 环境：uv；`uv run python …`
- 长任务：tmux启动，日志直接重定向到文件；macOS超过5分钟加`caffeinate -imd`
- 数值批任务：`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1`；无头绘图`MPLBACKEND=Agg`

## <服务器名> · 在用

- **登录**：`ssh <别名或完整命令>`
- **用途**：<P19训练 / baseline评测>
- **费率**：<¥x/h，开机即计费；自有机器写“无租金，注意电源与睡眠”>
- **资源**：GPU <型号 显存> · CPU <核数> · 内存 <GB> · 数据盘 <路径 可用量>
- **环境**：<python绝对路径或 .envs/ 名称，torch/CUDA版本>
- **目录**：代码 `<远端项目路径>` · run输出 `<远端路径>/work/NN_slug/runs/`
- **注意**：<同时只跑一个GPU重任务 / 重启后需手动恢复 等>

## 通用操作

| 做什么 | 命令 |
|---|---|
| 部署已提交的代码 | `tools/remote.sh deploy <服务器> <NN_slug>` |
| 取回run | `tools/remote.sh pull <服务器> <NN_slug>` |
| 查看GPU占用 | `ssh <服务器> nvidia-smi` |

## 备份

<!-- 不进git的内容如何备份：runs、data、权重。写清位置与频率。 -->

## 已释放

- <服务器名>：YYYY-MM-DD释放；run已回传至 `work/NN_slug/runs/`

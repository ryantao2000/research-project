# <项目名>

<!-- 门面文件：一屏以内，很少改动。状态写在desk看板，服务器写在OPS。 -->

<一两句话：研究什么问题，想得到什么。>

**从这里开始读：** [desk/00_INDEX.md](desk/00_INDEX.md)（看板） → [01_OVERVIEW](desk/01_OVERVIEW.md)（方向） → [05_findings](desk/05_findings/00_INDEX.md)（已有结论）。

## 目录地图

| 目录 | 放什么 | 谁常看 |
|---|---|---|
| `desk/` | 看板、方向、目标、计划、结果专栏、概念、报告、疑问 | 我 |
| `lab/` | 实操notebook | 我 |
| `literature/` · `repos/` | 论文资料 · 参考代码仓库 | 按需 |
| `code/` | 方法代码与测试 | 模型 |
| `work/` | 按计划组织的执行区与run | 模型 |
| `data/` · `sync/` · `tools/` | 数据 · 对外交付 · 工作区工具 | 模型 |

## 环境

```bash
uv sync
```

<!-- 如有：运行测试、启动jupyter的命令。 -->

## 仓库说明

主仓库保存文本、代码和配置；`work/*/runs/`、`data/`原始数据、`repos/`仓库本体、`sync/`子仓库不进git，另行备份（见OPS）。

# research-project 0.6.1

一套轻量、可追溯的个人研究工作区组织方法。入口：[SKILL.md](SKILL.md)。本仓库根目录就是完整skill包。

- 研究方向、计划、执行证据、结果、学习和报告职责分明，目录按需建立。
- 文献每篇一个目录，集中保存来源、原文和提取；理解直接进入Concepts。
- Concepts用正文Markdown任务列表记录用户是否读懂，支持Typora交互。
- project.py只读检查本地链接与计划/Results目录配对，不管理授权或科学接纳。

## 使用

将完整包安装到项目所采用的skill目录，并记录使用的版本。先读架构与初始化说明，按项目实际需要实例化模板；升级前比较本地定制，不自动覆盖AGENTS、计划或阅读状态。

```bash
uv run python scripts/project.py --root /path/to/project check
```

`--include`缩小检查范围，`--exclude`排除项目声明的路径；独立Git目录自动剪枝。工具不检查标题锚点、提取准确性或科学结论，也不写索引。

[版本变化](CHANGELOG.md) · [来源与取舍](PROVENANCE.md)。

本地v0.6.1补齐Phase生命周期、重要INDEX模板与Concepts组织细则；版本标记不等于远程已发布。目录管理见[映射](references/index-management.md)，本轮验证见[验证记录](VALIDATION.md)。

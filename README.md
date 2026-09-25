# research-project 1.0

个人研究工作区的组织方法与模板。入口：[SKILL.md](SKILL.md)。

- **两个区域**：`desk/`是研究者本人的区域，用来阅读、勾选、提问；其余目录是模型的执行与证据区。
- **编号体系**：desk内部、计划、专栏、文章编号；论文与代码仓库用语义键；计划在plans、findings、work三处同号。
- **分层INDEX**：AGENTS → 各目录`00_INDEX.md`（维护规则 + 导航）→ 文件，模型按任务逐层读取。
- **Goal节奏**：阶段性成果节点，收尾时按清单整理疑问、inbox、方向与git。
- **专栏阅读**：findings与concepts都是专栏式讲解文章，首尾带Typora勾选框。

## 使用

把整个仓库放到项目采用的skill目录（如`.claude/skills/research-project/`）。在新项目中请模型“用research-project初始化项目”，或“把旧项目迁移到research-project结构”。之后的日常工作按项目自己的AGENTS与INDEX进行，无需再加载skill。

模板按项目目录结构组织在[templates/](templates/)，对照表见SKILL.md。

[版本记录](CHANGELOG.md)

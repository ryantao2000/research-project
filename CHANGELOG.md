# 版本记录

## 1.0.0 · 2026-09-26

重新设计：skill只负责初始化与迁移，内容以模板为主。

- 新结构：`desk/`研究者区域（00看板、01方向、02决定、03目标、04计划、05结果专栏、06概念专栏、07报告、08疑问、09外部输入）；顶层`lab/ literature/ repos/ data/ code/ work/ tools/ sync/ tmp/ archive/`不编号。
- Results改为`05_findings/`专栏：总结果页“一眼看懂”+ 每计划一个专栏，专题为讲解型文章；细节证据移到`work/NN_slug/evidence/`。取消CLAIMS台账。
- 实验与run合并为按计划组织的`work/NN_slug/`，取消NN-M实验编号；run记录`RUN.json`与`code_commit`。
- 计划模板采用Phase中心结构（Phase｜中心问题｜关键工作说明｜核心产出），建立后默认汇报用途与路线。
- 新增Goal收尾清单、疑问暂存与沉淀流程、DECISIONS、首尾阅读勾选框、lab notebook（nbstripout）、OPS服务器卡片、`tools/remote.sh`部署回传范例。
- literature与repos分开，各有类别目录与`_inbox`；upstream、facts、UNKNOWNS不再单独设置。
- 删除`project.py`检查工具、测试、references、VALIDATION、PROVENANCE与旧模板；授权原则只在AGENTS模板写一次。

## 0.6.1 · 2026-09-11

- 补齐Phase导航、授权/执行状态分离、追加、修订、暂停、恢复、取消和完成规则。
- 重写Concepts总入口及专题模板，补齐拆分/合并、reference、读懂记录和按需CONCEPT_PLAN。
- 增加项目、结果、数据、实验、上游、运行、报告和同步INDEX模板及落点映射。
- 修复行内公式反斜杠，明确独立公式和Typora正文任务列表格式。
- 工具保持只读链接/目录关系检查；不迁移项目历史，不自动发布。

## 0.6.0 · 2026-09-11

- 以ChoicePFN当前职责分层整合LLMUCBSurvey的授权连续性、完整包来源与版本记录经验；不是把0.5.3覆盖0.5。
- 文献每篇一个语义键目录，SOURCE.md、paper.pdf、extracted.txt按实际取得创建；分类、登记与入库规则集中在INDEX，不强制digest或独立INGESTION。
- Concepts用逐篇复选框表示用户确认读懂，未勾选不等于未读，保留卡点与旧状态。
- 工具收敛为链接与目录关系检查，不要求自动盘面或认知台账。
- code保存方法实现及其测试，实验/报告专用脚本就近，跨任务工具使用scripts；不默认建根lib/tests或Results/repro。
- 旧目录、授权、原始材料与已接受运行不因升级自动迁移；报告和学习按真实需要组织，不固定章节或自动PDF。

### 0.6.1 实际初始化问题补充

根据v0.6.0初始化项目的只读检查，补充：INDEX存在不等于细则齐全；阶段执行表可由Results唯一维护；无Git项目可明确记录源码快照与文件校验；平铺Concepts按学习规模扩展，历史教程链接不冒充新教学交付。公开包不包含来源项目原文、路径、数据或实验结果。

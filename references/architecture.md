# 目录职责

目录地图不是初始化清单，有实际内容才创建。旧项目保留其稳定编号与路径。

| 位置 | 唯一主要职责 |
|---|---|
| 00_knowledge/00_INDEX.md | 导航、简短近况和真正需要决定的事项，不复制各处完整状态 |
| 00_knowledge/01_OVERVIEW.md | 研究问题、方向和范围 |
| 00_knowledge/DECISION_LOG.md | 重要方向及规则决定，追加历史 |
| 00_knowledge/02_subplans/ | 计划设计、范围授权和阶段；INDEX给导航与生命周期细则 |
| 00_knowledge/03_results/ | 与计划配对的实际结果、解释与来源；长过程记录按需放log |
| 00_knowledge/03_results/CLAIMS.md | 值得长期引用的主张；普通环境失败不必登记为主张 |
| 00_knowledge/04_dialog/ | 实际问答，不伪造讨论史 |
| 00_knowledge/05_concepts/ | 学习解释与用户读懂标记 |
| 00_knowledge/06_facts/ | 值得长期引用的外部事实核验，带日期与来源；并非每个网页都立卡 |
| 00_knowledge/07_reports/ | 按受众组织的报告、必要图表和讲稿 |
| 00_knowledge/08_goals/ | 可选的短期优先级，不复制技术授权 |
| 00_knowledge/09_meetings/ | 按需区分01_source原始输入与02_extracted助手提取 |
| 00_knowledge/10_revision/ | 有审稿任务时建立逐项意见、证据与回复关系；旧项目编号不重排 |
| 01_literature/ | 每篇一个key目录；来源、原文、提取；INDEX分类与入库规则 |
| 02_data/ | 原始数据与跨run可复用派生数据，权限和manifest按实际要求 |
| 03_experiments/ | NN-M实验编排、配置、专用分析和scratch |
| 04_upstream/ | 第三方源码或原始工程，只读来源及版本 |
| 05_runs/ | 实际配置、日志、指标、成本与原始产物，失败保留 |
| 06_sync/ | 各自独立Git的交付或共享仓库，外层INDEX说明关系 |
| code/src/ | 方法、模型、生成器、基线和评测实现的唯一开发位置 |
| code/tests/ | 方法测试，随方法代码管理 |
| scripts/ | 真正跨任务复用的工作区工具 |
| 99_archived/ | 停止维护的历史，保留引用和去向 |

根AGENTS说明常驻原则与任务路由，README指向入口，OPS说明当前环境。方法位置可改名或独立Git，但权威只能明确指定；实验目录调用方法，不复制开发线。单次实验分析就近放实验目录，单份报告绘图就近放报告目录。根lib/tests不是默认结构，旧项目不自动搬动。

复现是一类任务，在对应Results说明原文设定、实际版本与执行、差异、产物和未验证范围；无需另建repro台账。材料身份、执行事实、研究判断、学习理解、报告表达互相引用，不能互相替代。

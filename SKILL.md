---
name: research-project
description: 初始化、迁移或调整个人研究工作区及其模板，以 Goal 推进研究，维护阅读与资料索引，将逐计划分析和长期理解沉淀到 concepts，并组织实验与交付。
metadata:
  version: "1.3.0"
---
# research-project v1.3

本 skill 用于初始化、迁移、结构调整及取用模板。日常工作由项目根 AGENTS.md 自足指导，只读任务相关内容；不要每次重读 skill 或全部索引。

## 原则与结构

Goal统领阶段研究判断；Plan以Phase表组织设计；work保存执行事实；concepts汇集逐计划分析与跨计划理解；reports用于正式报告；sync用于选择性交付。阅读入口保留INDEX，减少的是重复状态与无必要的中间文件。

```text
project/
├── README.md                         简介、当前Goal、主要入口
├── AGENTS.md                         自足的工作原则与路由
├── OPS.md                            按需：当前环境、机器、运行恢复
├── pyproject.toml / uv.lock           有Python计算时建立
├── .agents/skills/research-project/   本skill与templates的随项目副本
├── goals/
│   ├── 00_INDEX.md
│   └── GNN_slug/00_INDEX.md           Goal正文兼导航；ref/按需
├── plans/
│   ├── 00_INDEX.md
│   └── NN_slug.md                     Phase总览与逐阶段设计
├── concepts/
│   ├── 00_INDEX.md
│   ├── 00_plan-analyses/
│   │   ├── 00_INDEX.md                逐计划分析阅读目录
│   │   └── NN_slug/00_INDEX.md        至少一篇分析；可拆文章、附ref/notebook
│   └── NN_topic/00_INDEX.md           长期主题专栏，文章与ref按需
├── reports/
│   ├── 00_INDEX.md
│   └── RNN_slug/                      00_INDEX.md、实际报告源文件、可选ref/
├── work/NN_slug/                      README、configs、scripts、tables、figures、runs
├── code/                             跨计划复用代码
├── data/                             原始/派生数据及README中的切分说明
├── literature/                       00_INDEX.md、inbox/、文献key目录
├── repos/                            00_INDEX.md、inbox/、原仓库名目录
├── sync/                             00_INDEX.md、交付副本
├── tools/                            确需复用的工具
├── tmp/
└── archive/                          按需
```

目录有内容时再建，但concepts启用时默认建立00_plan-analyses专栏。goals、concepts、plans、reports、literature、repos、sync一旦启用就维护00_INDEX.md；多篇文章的concepts主题另有专题INDEX。没有独立desk、findings、meetings、questions或lab体系。

## 内容与状态归属

- **Goal**：每个目标一个子目录，00_INDEX.md直接写阶段问题、意义、范围、路线、关键决定、完成条件和最终判断，不再套goal.md。goals总索引维护阶段状态。Goal路线链接Plan并解释依赖，不抄计划Phase进度。
- **Plan**：plans总索引维护状态（如执行中·Phase 2）与分析入口；正文保留Phase总览表和各Phase设计，按真实任务划分，可只有一个Phase；Phase 0仅在需要先验证关键输入时增加。工程/写作任务不硬凑科学假说。
- **逐计划分析**：每个完成的Plan至少有`concepts/00_plan-analyses/NN_slug/00_INDEX.md`，与plans/work同号同slug。该文件本身就是分析，不为一篇文章另造导航。复杂时再拆子文章，原文件提供总判断与阅读顺序。没有分析不标为完整交付；暂停/终止且有实际工作时留阶段分析，未执行草案不编造结果。
- **长期主题**：按问题综合多个Plan的理解，不与计划编号对应。概念、文献、方法和实验认识一起讲，不复制逐计划分析全文。
- **work**：运行事实、完整输出、表图与简短结论；正式run一份RUN.json与日志。正文数字直接链接表/run，重要负结果和不确定性不能因精简而省略。
- **报告**：每份报告独立RNN_slug目录，INDEX写对象、用途、当前版本及入口，正文是实际Markdown/TeX/幻灯片等。ref放专用模板、批注等；不预建多套版本。
- **ref**：Goal、分析、主题和报告可就近保存专用原件；已有literature/repos材料用链接，不反复复制。取消meetings不等于删除旧原件。
- **sync**：源文件只维护一份，按白名单导出。它与计算部署/回传分开；不在交付副本手工修改同一正文。

INDEX是读者界面：新增/移动内容、改变版本/状态/阅读顺序时更新相关索引，不每轮遍历全项目。根README只提示当前方向与入口。计划工作状态在plans INDEX，执行状态在run，阅读导航在concepts；不维护多份相同流水账。

## 阅读、资料与文件节制

阅读勾选仅由研究者明确确认：单篇Plan分析的勾选放逐计划分析总INDEX；拆成多篇后，子文章勾选放该分析目录INDEX，总INDEX只保留链接。长期主题的文章勾选放专题INDEX；只有单篇并直接挂总INDEX时就在总INDEX维护。每篇一处，正文不再首尾重复，未勾选不等于未读。

literature按author年份-topic命名，SOURCE记准确版本和来源；INDEX管检索、关联与材料状态。repos默认保留原仓库名，重名/过于通用时用owner--repo；文献与代码通过索引关联，不要求同名。repos INDEX记录原URL、固定commit/tag、本地位置和用途，版本变化时更新。

新材料直接放各自inbox，先简记名称和用途；实际使用时再查重、确认来源与归位。正常归档移动原件，复制后已确认目标完整的重复件可清掉；不能删掉唯一原件。每个inbox只保留一个README.md简记日期、原名、去向与处理状态；整理完可清空材料但保留该文件。不强制清空inbox作为Goal结束条件，也不按每次文件操作生成独立台账。

默认不生成evidence/audit、限制清单、补充说明、交接、逐图来源账、验证报告。必要检查仍做：相关测试、小试跑、结果来源和一次传输校验；检查不等于另造文档。用户要求、交付规范或具体异常确有需要时才增加诊断文件。影响结论的限制写在相关正文，失败/恢复记日志，重要转向记Goal。

notebook就近放concepts或work，默认共用项目环境；长计算由脚本生成表，修改后验证受影响范围，不默认全部重跑。数据可见范围依项目已确认协议，不从模板推断切分年份或授权。

## 初始化、迁移与随项目携带

1. 从对话提取研究方向与当前Goal，未知且影响工作时再问。使用模板生成自足AGENTS、README和实际需要的文件；移除空节及填写注释，不预建全套空目录。AGENTS必须包含组织原则、Plan分析完成条件、索引职责、资料处理、运行/发布边界，不把核心约束外包给本skill。
2. 将本skill的`SKILL.md`和完整`templates/`复制到项目`.agents/skills/research-project/`，不复制源仓.git、临时文件或递归复制整个项目。项目已有副本时比对版本和本地定制后合并，不直接覆盖。根AGENTS标明模板位置；日常无需加载，创建新文档才查对应模板。宿主可用其他skill目录时可适配位置并同步路由，避免多个活动副本。
3. 部署/交接时将根AGENTS与该skill副本纳入代码包，避免远端找不到模板；这不自动授予传输/发布权限。环境与命令按真实Windows/macOS/Linux选择，不默认Bash、tmux、WSL或软链接。
4. 迁移先用一个活跃Goal及关联Plan作样板，保留旧材料与编号。旧findings可转入对应逐计划分析，再择要沉淀长期主题；旧meetings按需归Goal的ref，未归属的留旧归档。重要路径映射写根README即可。未纳入范围的旧项目不随skill升级自动改动。
5. 同机试行可明确引用旧位置；跨机独立运行应包含所需数据、外部代码、run或给出实际获取方式。不能依赖另一台机器的绝对路径，未知远端缺口如实说明。

Goal收尾写判断、依据、下一步，检查所属已完成Plan是否有分析，再更新相关索引。不强制inbox清点、逐Phase提交或全项目审计。Git提交和发布沿用已有授权，使用skill本身不扩张授权。

## 模板路由

以下路径相对本skill；只取当前需要的模板。

| 用途 | 模板 → 项目位置 |
|---|---|
| 根入口 | [README](templates/README.md)、[AGENTS](templates/AGENTS.md)、[OPS](templates/OPS.md)、[gitignore](templates/gitignore) → 根目录 |
| Goal | [总索引](templates/goals/00_INDEX.md)、[目标正文](templates/goals/goal-INDEX.md) → goals/00_INDEX.md、goals/GNN_slug/00_INDEX.md |
| Plan | [总索引](templates/plans/00_INDEX.md)、[计划](templates/plans/plan.md) → plans/ |
| concepts | [总索引](templates/concepts/00_INDEX.md)、[分析专栏](templates/concepts/analyses-INDEX.md)、[计划分析](templates/concepts/analysis-INDEX.md)、[专题索引](templates/concepts/topic-INDEX.md)、[主题文章](templates/concepts/article.md) → 对应阅读位置 |
| 报告 | [总索引](templates/reports/00_INDEX.md)、[报告入口](templates/reports/report-INDEX.md) → reports/00_INDEX.md、reports/RNN_slug/00_INDEX.md |
| 执行 | [任务说明](templates/work/task-README.md)、[RUN](templates/work/RUN.json) → work/NN_slug/及runs/run_id/ |
| 数据 | [data](templates/data/README.md) → data/README.md |
| 文献 | [索引](templates/literature/00_INDEX.md)、[来源](templates/literature/SOURCE.md) → literature/ |
| 外部代码 | [索引](templates/repos/00_INDEX.md) → repos/00_INDEX.md |
| inbox | [进出记录](templates/inbox/README.md) → literature/inbox/README.md、repos/inbox/README.md |
| 同步 | [sync](templates/sync/00_INDEX.md) → sync/00_INDEX.md |

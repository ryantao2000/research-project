---
name: research-project
description: 初始化个人研究工作区（AGENTS、desk阅读区、编号与各级INDEX管理体系），或把旧研究项目迁移到这套结构；也在需要计划、结果专栏、概念专栏、Goal、服务器手册等模板时使用。日常工作遵循项目自己的AGENTS与INDEX，无需加载本skill。
metadata:
  version: "1.0.0"
---
# research-project v1.0

一套个人研究工作区的组织方法。skill只负责**初始化和迁移**：生成项目的AGENTS、目录骨架和各级INDEX。之后的日常工作由项目内的AGENTS和INDEX驱动。

## 方法论：六条原则

1. **两类读者，两个区域。** `desk/`是研究者本人的区域：阅读、勾选、提问、交互，写作要可读、篇幅受控。其余目录是模型的执行与证据区：要可执行、可追溯，研究者不必进入。
2. **序号管顺序与记忆，语义键管身份。** desk内部、计划、专栏、专栏文章一律编号；论文与代码仓库用语义键；顶层目录不编号。
3. **同号贯穿。** 计划19在`desk/04_plans/19_slug.md`、`desk/05_findings/19_slug/`、`work/19_slug/`三处同号同slug。
4. **分层披露。** AGENTS（常驻原则、编号表、路由）→ 各目录`00_INDEX.md`（维护规则 + 导航）→ 具体文件。模型只读当前任务涉及的层级。
5. **阅读状态只由研究者勾选。** 阅读型文档首尾带勾选框；模型仅在研究者明确说“读懂了”时代为勾选，并同步到INDEX显示。
6. **Goal是节奏。** 每个Goal是一个阶段性成果节点；Goal收尾时按固定清单整理（见goals INDEX模板）。

研究主循环：

```text
Goal开启 → 计划NN → 执行 work/NN → 结果专栏 findings/NN → 概念消化 → 报告 → Goal收尾整理
                                          ↑ 阅读中的疑问 → 08_questions → 沉淀回专栏
```

## 项目结构

```text
<project>/
├── AGENTS.md (CLAUDE.md → AGENTS.md)   模型常驻：原则、编号、路由
├── README.md                             门面：是什么、从哪读、目录地图、装环境
├── OPS.md                                服务器与环境手册（每台机器一张卡片）
├── .gitignore
├── desk/          研究者区域，内部编号
│   ├── 00_INDEX.md      看板          01_OVERVIEW.md   方向
│   ├── 02_DECISIONS.md  决定史        03_goals/        G01…
│   ├── 04_plans/        NN_slug.md    05_findings/     NN_slug/ 结果专栏
│   ├── 06_concepts/     NN_专栏/      07_reports/      R01…
│   ├── 08_questions/    Q001…         09_meetings/     source / extracted
├── lab/           实操notebook，编号，配nbstripout
├── literature/    论文与文字资料：类别目录 + _inbox
├── repos/         参考代码仓库：类别目录 + _inbox（仓库本体不进外层git）
├── data/          项目数据（原始数据不进git）
├── code/          跨计划共用的方法代码包与测试
├── work/          NN_slug/ 按计划的执行区：configs scripts tables evidence log runs
├── tools/         跨计划工作区工具（如服务器同步）
├── sync/          对外交付：独立git或不进git的副本，只跟踪00_INDEX
├── tmp/           临时文件，不进git
└── archive/
```

目录按需建立：没有服务器就不写OPS卡片，没有对外交付就不建sync，纯阅读项目可以没有work与code。

## 流程

### 新建项目

1. 问清：研究问题（一两句）、是否有服务器、是否需要对外交付仓库、是否要lab notebook、concepts打算从哪些专栏起步。
2. 按下表复制模板到项目，填入真实内容；删掉无内容的小节和模板注释。`templates/gitignore`复制为`.gitignore`，`templates/lab/gitattributes`复制为`lab/.gitattributes`。
3. 创建`CLAUDE.md → AGENTS.md`软链接。
4. `git init`并首次提交；启用lab时在项目根执行`nbstripout --install --attributes lab/.gitattributes`（需已安装：`uv tool install nbstripout`）。
5. 向研究者汇报：建立了哪些目录、desk从哪里开始读、下一步建议开第一个Goal。

### 迁移旧项目

1. 在旧项目旁新建目录并按“新建项目”初始化；旧项目保留为只读归档，不在原地改造。
2. 先迁一个活跃计划作为样板：计划正文、findings专栏、work目录、相关concepts与literature。研究者试读确认后再批量迁移。
3. 旧的大体量产物（runs、权重、数据）不复制，新文件以路径引用旧位置，并在`archive/00_INDEX.md`或对应INDEX记录映射。
4. 旧编号尽量保留（计划NN、G、R），保证记忆连续。

### 日常

不加载skill；按项目AGENTS与相关INDEX工作。项目规则需要调整时直接改项目AGENTS或对应INDEX；通用做法值得回收时，再由研究者要求更新本skill。

## 模板对照

| 模板 | 落点 |
|---|---|
| `templates/AGENTS.md` `README.md` `OPS.md` `gitignore` | 项目根 |
| `templates/desk/00_INDEX.md` `01_OVERVIEW.md` `02_DECISIONS.md` | `desk/` |
| `templates/desk/03_goals/00_INDEX.md` · `goal.md` | goals入口 · 单个`G<NN>_slug.md` |
| `templates/desk/04_plans/00_INDEX.md` · `plan.md` | 计划入口 · 单个`NN_slug.md` |
| `templates/desk/05_findings/00_INDEX.md` · `column-INDEX.md` · `topic.md` | 总结果 · 专栏`NN_slug/00_INDEX.md` · 专题文章 |
| `templates/desk/06_concepts/00_INDEX.md` · `column-INDEX.md` · `article.md` | 学习地图 · 专栏入口 · 文章 |
| `templates/desk/07_reports/00_INDEX.md` | 报告入口 |
| `templates/desk/08_questions/00_INDEX.md` · `question.md` | 疑问暂存 · 单个`Q<NNN>_slug.md` |
| `templates/desk/09_meetings/00_INDEX.md` | 外部输入入口 |
| `templates/lab/00_INDEX.md` · `gitattributes` | `lab/` |
| `templates/literature/00_INDEX.md` · `SOURCE.md` | 文献入口 · 每篇`<key>/SOURCE.md` |
| `templates/repos/00_INDEX.md` | 代码仓库登记 |
| `templates/work/00_INDEX.md` · `plan-INDEX.md` · `log.md` | 执行区入口 · `work/NN_slug/00_INDEX.md` · 执行日志 |
| `templates/data/00_INDEX.md` `templates/sync/00_INDEX.md` | 对应目录 |
| `templates/tools/remote.sh` | 服务器部署与回传范例，按OPS改写 |

## 共通写作约定

- 中文为主；代码标识、论文原名、标准指标保留英文。
- 行内公式`\(…\)`，独立公式用前后各自独占一行的`$$`；不用代码块呈现数学。
- 勾选框写成`- [ ] `（方括号内有空格），放在正文，不放进表格或代码块。
- 模板中的`<!-- -->`注释是给模型的填写说明，实例化后删除。

# <项目名> · 模型工作原则

<!-- 常驻文件，目标4KB以内。只写每次都需要的原则、编号和路由；目录细则写在各自00_INDEX。 -->

<一句话研究目标。> 方向详见 [OVERVIEW](desk/01_OVERVIEW.md)，当前状态见 [看板](desk/00_INDEX.md)。

## 边界

- 本次范围由用户当前要求决定；只读任务不改文件。已获批的计划在范围内连续完成，Phase切换不重复请求批准；完成交付后停止，不为用完预算追加工作。
- 新的付费计算、超出计划上限、push/上传/对外发布、删除原始数据或run，需用户明确同意。
- 不读取、打印或提交`.env`与密钥；代码只通过环境变量名引用凭据。
- 保护原件：`data/`原始数据、`literature/`原文、`repos/`外部仓库、`09_meetings/01_source/`、已接受的run，只读不改。
- 阅读勾选只在用户明确表示读懂时修改。

## 编号

| 对象 | 格式 | 位置 | 规则 |
|---|---|---|---|
| 目标 | `G<NN>_slug` | desk/03_goals | 全局唯一，不复用 |
| 计划 | `NN_slug`，行文写P<NN> | desk/04_plans · desk/05_findings · work | 三处同号同slug；Phase从0起，0为基础核验 |
| 结果专题 | 专栏内`NN_slug` | desk/05_findings/NN_slug/ | 同号ipynb可放lab |
| 概念专栏/文章 | `NN_slug` | desk/06_concepts/ | 编号分配后不改；阅读顺序以INDEX为准 |
| 报告 | `R<NN>_slug` | desk/07_reports | 版本记在报告目录内 |
| 决定 | `D<NN>` | desk/02_DECISIONS.md | 只追加 |
| 疑问 | `Q<NNN>_slug` | desk/08_questions | 必须写明去向 |
| 外部输入 | `G<NN>-S<nn>` | desk/09_meetings | 按Goal分卷 |
| notebook | `NN_slug.ipynb` | lab | 阅读顺序以INDEX为准 |
| run | `NN-slug-YYYYMMDD[-rN]` | work/NN_slug/runs | 以所属计划号开头 |
| 文献/代码仓库 | 语义键`author年份-主题` | literature · repos | 同一工作两边同key |

## 按任务读取

先读与任务相关的入口，不通读全仓。

| 任务 | 入口 |
|---|---|
| 了解现状、待决定事项 | [desk/00_INDEX.md](desk/00_INDEX.md) |
| 开启或收尾Goal | [desk/03_goals/00_INDEX.md](desk/03_goals/00_INDEX.md) |
| 建立、修订、恢复计划 | [desk/04_plans/00_INDEX.md](desk/04_plans/00_INDEX.md) |
| 执行实验、写脚本、跑run | [work/00_INDEX.md](work/00_INDEX.md)，然后`work/NN_slug/00_INDEX.md` |
| 使用服务器 | [OPS.md](OPS.md) |
| 写或更新结果专栏 | [desk/05_findings/00_INDEX.md](desk/05_findings/00_INDEX.md) |
| 讲解、写学习材料 | [desk/06_concepts/00_INDEX.md](desk/06_concepts/00_INDEX.md) |
| 处理疑问 | [desk/08_questions/00_INDEX.md](desk/08_questions/00_INDEX.md) |
| 入库论文 / 代码仓库 | [literature/00_INDEX.md](literature/00_INDEX.md) · [repos/00_INDEX.md](repos/00_INDEX.md) |
| 写报告、对外交付 | [desk/07_reports/00_INDEX.md](desk/07_reports/00_INDEX.md) · [sync/00_INDEX.md](sync/00_INDEX.md) |

## 代码与执行

- 另一个计划会调用的代码放`code/`（方法包与测试）；只服务本计划的放`work/NN_slug/scripts/`；临时文件放`tmp/`。
- 服务器只运行已提交的代码：部署前提交，run记录`code_commit`。部署与回传命令见OPS。
- 每个run记录配置、commit、开始结束时间与资源；失败run保留，恢复另起run并注明来源。
- 结果数字来自`work/NN_slug/tables/`或run原始产物，写进findings时链接来源；lab notebook只做探索。
- 环境用uv：`uv run python …`。

## 写作

- 中文为主；代码标识、论文原名、标准指标保留英文。
- 行内公式`\(…\)`，独立公式用前后独占一行的`$$`。
- desk中的阅读型文档（计划、结果专题、概念文章、报告）首尾保留勾选框。
- 区分已核验事实、推导与假说；给出样本量、基线和不确定性；负结果和被推翻的结论保留并注明。
- 读者在正文中写的`> ❓`是待回答的疑问，处理方式见questions INDEX。

## Git

- 获批计划写明“包含本地提交”时，每个Phase完成与Goal收尾各提交一次，信息格式`P<NN> Phase<k>: …`或`G<NN> 收尾: …`；只提交本任务相关文件。
- push由用户执行或明确授权后执行。`sync/`下每个仓库独立提交与push。

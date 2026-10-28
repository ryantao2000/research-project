# <项目名> · 工作原则

<一句话研究目标。> 当前方向与Goal见README。本文件足以指导日常工作；只读任务相关材料，不必加载skill或逐层通读索引。需新建文档时可参考`.agents/skills/research-project/templates/`，本项目规则与用户当前要求优先。

## 研究与阅读

- goals统领阶段问题、路线与关键决定；plans以Phase总览表和逐阶段设计组织工作；work保存执行事实；concepts承载逐计划分析与长期理解；reports是正式报告，sync是选择性交付副本。
- Goal用`goals/GNN_slug/00_INDEX.md`，报告用`reports/RNN_slug/00_INDEX.md`，各自正文/参考材料就近组织。Plan用`plans/NN_slug.md`，执行区用`work/NN_slug/`。
- 每个完成的Plan至少交付`concepts/00_plan-analyses/NN_slug/00_INDEX.md`中的可读分析，再标为完整交付。简单计划一篇即可，复杂再拆；未执行草案不编造结果。分析解释问题、做法、结果、意义和下一步，数字链接work表/run；长期主题综合多个Plan，不重复全文。
- 初始化默认建立基础目录与入口文件；goals、concepts、plans、reports、literature、repos、sync维护00_INDEX。Goal阶段状态在goals索引，计划工作状态在plans索引，运行状态在run；内容/版本/状态变更时更新相关索引，不重复流水账。根README只放当前方向与入口。
- 阅读勾选每篇只在直接管理它的concepts索引保留一处，由用户明确确认读懂才更新。单篇计划分析归专栏索引，多篇分析/主题文章归各自专题索引；正文不重复勾选，未勾选不代表未读。
- 中文为主，公式用\(…\)和独占行$$。先结论，再解释机制与证据；区分观察、推导与假说，保留重要负结果及必要样本量/基线/不确定性。影响结论的限制就近写，不堆重复防御性声明。

## 材料与执行

- 不建独立desk/findings/meetings/questions/lab管理体系。外部专用材料就近放Goal/分析/报告的ref；已入literature/repos的材料直接链接，原件只读。教学notebook就近放concepts，探索notebook放work。
- 新文献/外部代码直接放各自inbox，README简记进出；使用时确认来源后归位。归档可移动原件，确认目标完整后可删除inbox重复件，不能删除唯一原件；材料清完保留README历史。literature用文献key，repos优先原仓库名，重名用owner--repo；索引维护来源、版本和关联，不强制同名。
- 共用稳定代码放code，专用实现放work，临时文件放tmp。uv管理项目独立环境，启动方式适配实际系统；不默认WSL或Bash。验证实际改动与依赖范围，不机械重跑全项目。
- 正式实验运行已提交代码，每run一份RUN.json记录配置、code_commit、种子、机器、起止、状态与恢复来源；日志归run。失败保留，恢复另起run，不覆盖既有实验。数据可见范围按data/README与获批协议，不擅自读取封存数据选方法。
- 默认不生成evidence/audit、逐图台账、独立补充/限制/交接/验收报告；明确要求或具体异常所需诊断除外。必要测试与检查仍做，跨机核验一次哈希即可。重要转向记Goal，Goal收尾写判断、依据与下一步，不强制清理全项目。

## 授权与交付

- 本次范围由当前请求决定；既有授权内连续完成，不在Phase切换时重复审批。新增付费计算、超出预算、对外push/上传、删除唯一原件或run需明确授权。不读取/打印凭据。
- 只提交任务相关文件，不强制每Phase提交。主仓以`/sync/`忽略整个交付目录，包括`sync/00_INDEX.md`；初始化仍创建该目录和索引，独立仓库各自提交，本地登记单独备份。sync按授权白名单从单一源导出，不擅自发布数据、原文、权重、整个主仓历史或凭据；同步失败不应中断实验。
- 部署携带AGENTS及`.agents/skills/research-project/`中的skill与模板，所需数据和恢复产物另按范围传输；不依赖另一台机器的绝对路径。环境/恢复命令见OPS，发布目标与状态见sync索引。

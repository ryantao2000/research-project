# work · 执行区

按计划组织的执行现场：配置、脚本、结果表、细节证据、日志和run。与`desk/04_plans/NN_slug.md`同号同slug。

## 维护规则

### 每个计划的结构

```text
work/NN_slug/
├── 00_INDEX.md   执行导航：Phase → 配置 → 脚本 → run → 表格
├── configs/      实验配置（yaml），运行前提交
├── scripts/      本计划专用：启动、编排、汇总、绘图
├── tables/       脚本生成的整洁结果表（csv/parquet），findings与lab从这里读
├── evidence/     细节证据文档：逐格对照、诊断、复现对照
├── log.md        执行、偏离、失败、恢复、成本（按日期追加）
└── runs/         原始产物，不进git
```

计划开始执行时用research-project skill的`templates/work/plan-INDEX.md`与`log.md`建立；目录按需创建。

### 代码放哪里

- 另一个计划会调用的：`code/`（方法包与测试），通过`import`使用。
- 只服务本计划的：`work/NN_slug/scripts/`。
- 用完即弃的调试与试跑：顶层`tmp/`。
- 从外部仓库改写的代码注明来源key与版本。

### run

- **身份**：`NN-slug-YYYYMMDD[-rN]`，目录`work/NN_slug/runs/<run_id>/`。
- **记录**：每个run在目录内写`RUN.json`：run_id、Phase、配置路径、`code_commit`、执行机器、开始/结束时间、资源用量、状态（running / complete / failed）、恢复来源（`resumed_from`）。
- **只跑已提交的代码**：部署前提交，`code_commit`对应真实的git版本；服务器部署与回传见[OPS](../OPS.md)。
- **失败保留**：失败run不删不覆盖；恢复另起run并写`resumed_from`。
- **正式run前**：做与风险相关的小规模试跑与必要测试。
- **长任务**：分单元落盘，可识别已完成部分；同一run只有一个进程写入。

### 结果表

- 由`scripts/`从run产物生成，脚本可重复运行得到同一张表。
- 一行一个观测单位，列名写清指标与单位；表格旁放同名`.md`简述字段（可选）。
- findings中的数字从这里引用。

## 计划执行区导航

| 计划 | 状态 | 执行地点 | 入口 |
|---|---|---|---|
| P<NN> | 执行中 / 已完成 | 本机 / <服务器名> | [NN_slug](NN_slug/00_INDEX.md) |

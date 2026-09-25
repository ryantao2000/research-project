# repos · 参考代码仓库

外部代码仓库的只读副本。需要改写或适配的代码放`code/`或`work/NN_slug/scripts/`，并注明来自哪个仓库的哪个版本。

## 维护规则

- **结构**：`<类别>/<key>/`是clone下来的仓库本体（独立git，外层`.gitignore`忽略）；本页登记表是唯一跟踪的记录。
- **key**：与literature中对应论文同key；没有论文的仓库用`组织名-仓库名`。
- **版本**：clone后记录commit或tag；需要固定版本时checkout到该版本，不在仓库里直接改代码。
- **类别**：与literature保持相近的4–6个类别。
- **Inbox**：来不及归类的clone到`_inbox/<key>/`；Goal收尾时由模型建议类别，研究者确认后移动并登记。
- **重新获取**：仓库本体不进git，换机器时按登记表的URL和版本重新clone。

## 类别

| 目录 | 收什么 |
|---|---|
| `<category-a>/` | <一句话> |
| `_inbox/` | 待归类 |

## 登记表

| key | 来源URL | 锁定版本 | 用途 | 关联 |
|---|---|---|---|---|
| `<category>/<key>` | <https://github.com/…> | <commit或tag> | <作者实现 / 基线 / 参考架构> | literature key · P<NN> |

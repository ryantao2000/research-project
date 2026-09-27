# literature · 论文与文字资料

原文与机器提取的存放处。对论文的理解写进`desk/06_concepts/`，实验判断写进findings；这里只管“有什么、在哪、从哪来”。

## 维护规则

- **结构**：`<类别>/<key>/`，每篇一个目录，含`SOURCE.md`（research-project skill的`templates/literature/SOURCE.md`）、原文（`paper.pdf`）和提取文本（`extracted.txt`），按实际取得创建；多版本用明确文件名并存。
- **key**：`第一作者姓+年份-主题短语`，如`berbeglia2022-retail-choice`；同一工作的代码在repos用同一个key。
- **类别**：4–6个稳定类别，见下表；建好后尽量不移动目录。一篇只放一个类别，跨类别关系在登记表“备注”写明。
- **Inbox**：来不及归类的放`_inbox/<key>/`，只要放进来就算入库；Goal收尾时由模型建议类别，研究者确认后移动并登记。
- **入库**：先按标题、DOI或arXiv ID查重；SOURCE只记身份、版本、来源、文件对应和提取问题。只拿到摘要就写明是摘要。
- **其他资料**：slides、博客、网页存档放`other/`，同样一份一个目录。
- **Git**：PDF不进git（见`.gitignore`），另行备份；SOURCE.md与提取文本进git。

## 类别

| 目录 | 收什么 |
|---|---|
| `<category-a>/` | <一句话> |
| `other/` | slides、博客、网页等 |
| `_inbox/` | 待归类 |

## 登记表

| key | 标题 | 类别 | 关联 | 备注 |
|---|---|---|---|---|
| [key](category/key/SOURCE.md) | <标题（年份）> | <类别> | P<NN> · concepts NN | <代码见repos / 跨类别说明> |

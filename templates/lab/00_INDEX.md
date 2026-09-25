# lab · 实操notebook

用来亲手看项目：打开一条真实数据、跑一次生成器、把小例子送进模型、自己切片结果。notebook是探索工具；findings里引用的数字来自`work/NN_slug/tables/`和run产物。

## 维护规则

- **编号**：`NN_slug.ipynb`，编号分配后不改；阅读顺序以下表为准。
- **只读取**：通过`code/`中的函数、`data/`、`work/NN_slug/tables/`取数据，不直接解析run目录，也不写回这些位置；共用的加载函数放`_lib.py`。
- **从探索到结论**：notebook里发现值得保留的结果时，把计算改写成`work/NN_slug/scripts/`中的脚本，再写进findings。
- **Git**：已配置nbstripout，提交时自动去掉输出，本地文件保留输出；`lab/.gitattributes`不要删除。
- **打开**：`uv run --with jupyterlab jupyter lab`，或用VS Code打开。

## 导航

| 编号 | 看什么 | 对应阅读 | 用到的数据 |
|---|---|---|---|
| [01](01_slug.ipynb) | <例如：看一条真实选择记录> | [concepts NN/0k](../desk/06_concepts/NN_slug/0k_slug.md) | `data/…` |

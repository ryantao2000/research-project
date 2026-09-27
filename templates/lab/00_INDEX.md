# lab · 实操notebook

用来亲手看项目：打开一条真实数据、跑一次生成器、把小例子送进模型、手算一遍基线、自己切片结果。notebook是探索工具；findings里引用的数字来自`work/NN_slug/tables/`和run产物。

## 分栏

notebook按它陪读的材料分栏，和desk一一对应：陪concepts专栏的放`concepts/NN_slug/`，陪findings专题的放`findings/NN_slug/`，栏名与desk里的专栏同号同slug。每栏有自己的INDEX，写学习问题、阅读顺序和对应文章。

<!-- 每建一栏加一行；notebook列为该栏本数。 -->

| 分栏 | 学什么 | notebook | 对应阅读 |
|---|---|---:|---|
| [concepts/NN · slug](concepts/NN_slug/00_INDEX.md) | <一句话> | 1 | [concepts NN](../desk/06_concepts/NN_slug/00_INDEX.md) |
| [findings/NN · slug](findings/NN_slug/00_INDEX.md) | <一句话> | 1 | [findings NN](../desk/05_findings/NN_slug/00_INDEX.md) |

<!-- 可选：第一次来的推荐路线，例如“先读concepts NN的01–02，再用findings NN自己切结果”。 -->

## 运行

全部notebook用同一个uv环境，内核名 **<项目名> (lab)**（`<kernel>`）。第一次使用或换机器时，在仓库根目录执行一次：

```bash
bash lab/setup_env.sh
```

之后在Jupyter或VS Code里选这个内核即可；也可以`lab/.venv/bin/jupyter lab`启动。

- **版本锁定**：`requirements.txt`写意图（固定版本时在注释里写原因），`requirements.lock`锁定全部包的精确版本（跨平台）。改了`requirements.txt`后运行`bash lab/setup_env.sh --relock`。
- **可复用的范围**：换机器或仓库迁移后重跑脚本即可得到同样版本的包；`.venv`不进git，也不能拷贝搬家，需要时重建。
- **方法代码**：`code/`有`pyproject.toml`时，`setup_env.sh`会把它以可编辑方式装进同一环境。

<!-- 如有：代码、数据或权重暂时引用其他位置（例如迁移过渡期的旧工作区），写明由哪个共用模块引用、切换时改哪里。 -->

## 维护规则

- **位置**：`concepts/NN_slug/`或`findings/NN_slug/`，与desk中对应专栏同号同slug；一个notebook只放一栏，跨栏关系在栏INDEX写明。
- **编号**：栏内`NN_slug.ipynb`，从01起；编号分配后不改，阅读顺序以栏INDEX为准。
- **首个代码单元**：`import sys; sys.path.insert(0, '../..')`，让notebook找到lab根目录的共用模块。
- **共用模块**：多本notebook共用的加载与计算函数放lab根目录的`_<name>.py`（如`_lib.py`），在此列出各自负责什么。只读取，不写回证据文件。
- **只读取**：通过`code/`中的函数、`data/`、`work/NN_slug/tables/`取数据，不直接解析run目录。
- **规模**：每本在本地CPU上几分钟内跑完；需要训练或完整评估的计算放`work/NN_slug/scripts/`产出表，notebook只读取。演示机制时用小例子或少量步数。
- **从探索到结论**：notebook里发现值得保留的结果，把计算改写成`work/NN_slug/scripts/`中的脚本，再写进findings。
- **执行**：新建或改动后完整执行一遍（`jupyter nbconvert --to notebook --execute --inplace`），确认无报错再登记到栏INDEX。环境或共用模块改动后全部重跑一遍。
- **Git**：已配置nbstripout，提交时自动去掉输出，本地文件保留输出；`lab/.gitattributes`不要删除。

## 更新记录

<!-- 结构、环境或批量重跑时简记：日期、改了什么、是否全部重新执行通过。 -->

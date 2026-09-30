# luminescent-agent

**从文献到配方：面向发光材料的检索与推荐 Agent**

输入目标发光性能指标（发射波长、量子效率、基质体系等），输出候选材料体系、合成参数建议与可追溯的文献证据链。

---

## 为什么做这个

发光材料的研究流程里，最费时间的不是合成，而是"先搞清楚别人已经试过什么"：文献散落在几十种期刊里，性能数据以表格、图、正文三种形式存在，参数（掺杂浓度、烧结温度、保温时间、气氛）往往缺项。而这些恰恰是决定下一次实验该怎么做的东西。

这个项目要把这条链路打通：

```
文献 / 实验数据  →  结构化数据库  →  Agent 检索与推理  →  候选配方 + 参数建议  →  真实合成验证  →  结果回灌
```

目标不是做一个"论文问答机器人"，而是让每一次实验都建立在可验证的既有证据之上，并把新产出的数据沉淀回数据库——形成闭环。

## 当前状态

**第 1 阶段（数据管线地基）进行中。**

| 阶段 | 内容 | 状态 |
|---|---|---|
| 1 | 文献抓取、解析、去重、导出（Crossref 数据源） | 进行中 |
| 2 | 手写 Agent 循环（工具调用，不依赖框架） | 未开始 |
| 3 | RAG 检索与引用溯源 | 未开始 |
| 4 | 评估集与工程化（准确率 / 幻觉率 / 成本 / 延迟） | 未开始 |
| 5 | 发光材料专属的结构化抽取与配方推荐 | 未开始 |
| 6 | 部署、文档、可复现的实验验证报告 | 未开始 |

## 技术选型

- Python 3.12
- `requests` —— 调用 [Crossref REST API](https://api.crossref.org/swagger-ui/index.html)（免费、无需 API Key、覆盖主流出版社）
- `pytest` —— 单元测试
- 数据源层面的设计原则：**抓取、解析、存储严格分离**。以后接入 PubMed、自建实验数据库或真实实验数据时，只需新增一个 fetch 模块，上层代码不变。

## 环境准备

```powershell
git clone https://github.com/WYQy1/luminescent-agent.git
cd luminescent-agent
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

验证解释器正确：

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
```

输出路径必须包含 `.venv`。

## 使用

```powershell
# 抓取文献，保存为 JSON
python -m luminescent_agent.cli search "Eu3+ doped phosphor" --rows 50 --out data/papers.json

# 导出为 CSV（Excel 可直接打开，中文不乱码）
python -m luminescent_agent.cli export --src data/papers.json --out data/papers.csv

# 打开详细日志
python -m luminescent_agent.cli -v search "thermoluminescence LiF" --rows 20
```

## 项目结构

```
src/luminescent_agent/
├─ config.py          项目常量：目标期刊清单、默认检索词、数据目录
├─ models.py          领域对象（Paper），只有数据结构，不做 IO
├─ parse.py           Crossref 原始 JSON → Paper
├─ fetch_crossref.py  只负责调用 Crossref API，返回原始 JSON
├─ storage.py         JSON / CSV 落盘与读取
├─ utils.py           去重、排序、统计、格式化等纯函数
└─ cli.py             命令行入口，所有用户交互集中在这里
tests/
└─ fixtures/          手写的 API 响应样本，保证测试不联网
```

## 设计约定

- 每个模块只做一件事，函数不超过 30 行
- 单元测试**从不发起网络请求**，全部基于本地 fixture
- 所有文件读写显式指定 `encoding`
- 依赖保持最小：第 1 阶段只有 `requests` 和 `pytest`

## 已知限制

- 目前仅接入 Crossref 元数据，不含全文，因此暂无法抽取文中的性能参数
- 尚无评估集，因此没有可量化的效果指标
- 尚未接入真实实验数据（计划在获得实验室数据后接入）

## 许可

MIT

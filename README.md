# luminescent-agent

持续迭代的 Python 后端与 AI 应用开发学习仓库。按阶段递进，从 Python 语法基础到 FastAPI + SQLAlchemy 完整 Web API，每个阶段独立目录、独立环境。

## 学习路线

| 阶段 | 目录 | 内容 | 状态 |
|---|---|---|---|
| Stage 0 | [`stage0/`](./stage0/) | Python 进阶语法（装饰器、生成器）、FastAPI 入门路由、SQLAlchemy ORM 基础练习 | ✅ 进行中 |
| Stage 1 | [`stage1/`](./stage1/) | FastAPI + SQLAlchemy 2.0 + MySQL 完整任务管理 CRUD API，含分层架构与 pytest 自动化测试 | ✅ 已完成基础版 |

后续阶段将在此基础上扩展认证、数据库迁移、更多业务模块与 AI 应用集成。

## 目录结构

```
luminescent-agent/
├── stage0/                     # Python 进阶 + FastAPI 入门 + ORM 基础练习
│   ├── fastapi_basics/         # 路由、JSON、文件上传、请求体与参数校验示例
│   ├── ORM/                    # SQLAlchemy 模型定义、建表、CRUD 与 FastAPI 结合
│   ├── python_fundamentals/    # 装饰器、生成器、文件读取等进阶语法练习
│   ├── tests/                  # pytest 练习
│   └── README.md               # Stage 0 详细说明
│
├── stage1/                     # FastAPI + SQLAlchemy 完整任务管理 API
│   ├── app/
│   │   ├── main.py             # FastAPI 应用入口
│   │   ├── database.py         # 数据库引擎与会话管理
│   │   ├── models.py           # ORM 模型
│   │   ├── core/config.py      # 环境变量配置
│   │   ├── api/routes/         # RESTful 路由
│   │   ├── crud/               # 数据访问层
│   │   └── schemas/            # Pydantic 请求/响应模型
│   ├── tests/                  # pytest 自动化测试（独立测试库）
│   └── README.md               # Stage 1 详细说明
│
└── .gitignore
```

## 环境要求

- Python 3.11+
- MySQL 5.7+ / 8.0（Stage 1 需要）
- 每个阶段建议使用独立的虚拟环境

## 各阶段快速开始

### Stage 0 — 基础练习

```powershell
cd stage0
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

详见 [stage0/README.md](./stage0/README.md)。

### Stage 1 — 任务管理 API

```powershell
cd stage1
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 1. 创建 MySQL 数据库
#    CREATE DATABASE task_knowledge_db ...
#    CREATE DATABASE task_knowledge_test_db ...
# 2. 复制 .env.example 为 .env 并填入 MySQL 密码
# 3. 建表
python test_db.py
# 4. 启动
uvicorn app.main:app --reload
# 5. 打开 http://127.0.0.1:8000/docs
```

详见 [stage1/README.md](./stage1/README.md)。

## 安全注意事项

- `.env` 文件包含数据库密码、API Key 等敏感信息，已被 `.gitignore` 忽略，**不要提交到 Git**
- 不要在代码或 README 中硬编码密码、Token
- Stage 1 的测试使用独立的 `task_knowledge_test_db`，通过依赖注入隔离，不会操作开发库

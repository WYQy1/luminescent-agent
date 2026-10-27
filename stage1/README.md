# Stage1 — Task Knowledge API

基于 FastAPI + SQLAlchemy 2.0 + MySQL 的任务管理 RESTful API，是 luminescent-agent 学习路线的第一阶段项目。

## 功能列表

- 任务的增删改查（CRUD）
- 基于 Pydantic 的请求参数校验与响应序列化
- SQLAlchemy 2.0 ORM 模型映射
- 依赖注入管理数据库会话
- 独立测试数据库隔离，自动化测试覆盖全部接口

## 技术栈

| 技术 | 版本 | 用途 |
|---|---|---|
| FastAPI | 0.161.x | Web 框架 |
| Uvicorn | 0.54.x | ASGI 服务器 |
| SQLAlchemy | 2.1.x | ORM |
| PyMySQL | 1.2.x | MySQL 驱动 |
| Pydantic / pydantic-settings | 2.14.x / 2.16.x | 数据校验与配置管理 |
| pytest | 9.1.x | 测试框架 |
| httpx | 0.28.x | FastAPI TestClient 依赖 |

## 目录结构

```
stage1/
├── app/
│   ├── main.py              # FastAPI 应用入口
│   ├── database.py          # 数据库引擎、会话工厂、get_db 依赖
│   ├── models.py            # SQLAlchemy ORM 模型（Task 表）
│   ├── core/
│   │   └── config.py        # Pydantic Settings，从 .env 读取配置
│   ├── api/routes/
│   │   └── tasks.py         # RESTful 路由（5 个接口）
│   ├── crud/
│   │   └── task.py          # 数据访问层（增删改查）
│   └── schemas/
│       └── task.py          # Pydantic 请求/响应模型
├── tests/
│   └── test_tasks.py        # pytest 自动化测试
├── .env.example             # 环境变量模板
├── requirements.txt         # Python 依赖
├── test_db.py               # 手动建表脚本
├── test_insert.py           # 手动插入数据脚本
└── test_query.py            # 手动查询脚本
```

## 环境准备

### 1. 创建虚拟环境并安装依赖

```bash
cd stage1
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
```

### 2. 创建 MySQL 数据库

在 MySQL 中创建两个数据库：一个用于开发，一个用于测试。

```sql
CREATE DATABASE task_knowledge_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE task_knowledge_test_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env`，填入你自己的 MySQL 连接信息：

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=你的MySQL密码
DB_NAME=task_knowledge_db
```

> **注意：** `.env` 已被 `.gitignore` 忽略，不要提交到 Git。密码不要写进任何代码文件或 README。

### 4. 建表

```bash
python test_db.py
```

这会根据 `app/models.py` 中的 ORM 模型在 `task_knowledge_db` 中创建 `tasks` 表。

## 启动服务

```bash
uvicorn app.main:app --reload
```

启动后访问：

- **Swagger 文档（交互式 API）：** http://127.0.0.1:8000/docs
- **ReDoc 文档：** http://127.0.0.1:8000/redoc
- **健康检查：** http://127.0.0.1:8000/health

## API 接口一览

| 方法 | 路径 | 说明 | 成功状态码 |
|---|---|---|---|
| POST | `/tasks` | 创建任务 | 201 |
| GET | `/tasks` | 获取任务列表 | 200 |
| GET | `/tasks/{task_id}` | 获取单个任务 | 200 |
| PATCH | `/tasks/{task_id}` | 更新任务（局部更新） | 200 |
| DELETE | `/tasks/{task_id}` | 删除任务 | 204 |

## 运行测试

测试使用独立的数据库 `task_knowledge_test_db`，通过 `app.dependency_overrides` 覆盖 `get_db` 依赖，不会操作开发库 `task_knowledge_db`。

```bash
pytest tests/ -v
```

当前测试覆盖范围：

| 测试用例 | 覆盖接口 | 说明 |
|---|---|---|
| `test_hello` | `GET /health` | 健康检查 |
| `test_create_task` | `POST /tasks` | 创建任务并验证数据库落库 |
| `test_get_task_by_id` | `GET /tasks/{id}` | 先创建再查询，验证返回一致 |
| `test_get_task_not_found` | `GET /tasks/999999` | 查询不存在的 ID 返回 404 |
| `test_update_task` | `PATCH /tasks/{id}` | 局部更新并验证数据库 |
| `test_update_task_not_found` | `PATCH /tasks/999999` | 更新不存在的 ID 返回 404 |
| `test_delete_task` | `DELETE /tasks/{id}` | 删除后再查询返回 404 |

每个测试前后会自动清空 `tasks` 表，保证用例之间互不影响。

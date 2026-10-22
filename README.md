# luminescent-agent

持续迭代的 Python 后端与 AI 应用开发学习仓库。当前阶段：Python 进阶语法、FastAPI 入门、SQLAlchemy ORM 基础。

## 目录结构

```text
stage0/
├── fastapi_basics/          # FastAPI 路由、JSON、文件上传、请求体与参数校验示例
├── ORM/                     # SQLAlchemy 模型定义、建表、CRUD 与 FastAPI 结合
├── python_fundamentals/     # 装饰器、生成器、文件读取等进阶语法练习
└── tests/                   # pytest 练习
```

## 环境准备

建议使用 Python 3.11 或更新的兼容版本。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 运行 FastAPI 示例

```powershell
cd stage0
python -m uvicorn fastapi_basics.hello_api:app --reload
```

打开 `http://127.0.0.1:8000/docs` 查看接口文档。测试请求体与参数校验时，将启动模块替换为 `fastapi_basics.request_body:app`。

## ORM 示例说明

`stage0/ORM/` 目录：

- `models.py`：使用 `DeclarativeBase`、`Mapped`、`mapped_column` 定义 `User` 模型（对应 `users` 表）。
- `main.py`：创建数据库 `engine` 和会话工厂 `SessionLocal`。
- `create_tables.py`：调用 `Base.metadata.create_all(bind=engine)` 建表。
- `crud.py`：会话创建与读取等 CRUD 练习。
- `fastapi_orm.py`：将 FastAPI 接口与 SQLAlchemy 会话结合。

> ORM 示例依赖 SQLAlchemy；若连接 MySQL，还需安装对应数据库驱动。

## 运行练习与测试

在 `stage0` 目录中执行：

```powershell
python python_fundamentals\generators\generator_basics.py
python python_fundamentals\generators\batch_generator.py
$env:PYTHONPATH = (Get-Location).Path
python -m pytest
```

## GitHub 注意事项

不要提交 `.env`、`.venv/`、`__pycache__/`、访问令牌、密码或本机 IDE 配置。不要将真实 API Key 写入代码或 README。

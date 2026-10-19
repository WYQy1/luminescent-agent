# luminescent-agent

持续迭代的 Python 后端与 AI 应用开发学习仓库。当前阶段聚焦 Python 进阶语法与 FastAPI 入门。

## 当前阶段

- `stage0-python-backend-foundations/`：装饰器、生成器、文件读取、批量生成，以及 FastAPI 路由和请求参数校验。

后续可以随着学习进度增加 RAG、Agent 工作流和 AI 应用后端阶段；尚未开始的阶段暂不创建空目录。

## 环境准备

建议使用 Python 3.11 或更新的兼容版本。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 运行 FastAPI 示例

```powershell
cd stage0-python-backend-foundations
python -m uvicorn fastapi_basics.hello_api:app --reload
```

打开 `http://127.0.0.1:8000/docs` 查看接口文档。测试请求体与参数校验时，将启动模块替换为 `fastapi_basics.request_body:app`。

## 运行练习与测试

在阶段目录中执行：

```powershell
python python_fundamentals\generators\generator_basics.py
python python_fundamentals\generators\batch_generator.py
$env:PYTHONPATH = (Get-Location).Path
python -m pytest
```

## GitHub 注意事项

不要提交 `.env`、`.venv/`、`__pycache__/`、访问令牌、密码或本机 IDE 配置。不要将真实 API Key 写入代码或 README。

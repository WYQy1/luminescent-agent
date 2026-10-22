"""最小 FastAPI 应用：根路由与 hello 路由。"""
from fastapi import FastAPI

app = FastAPI(title="Stage 0 - FastAPI Basics")


@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI!"}


@app.get("/hello")
async def read_hello():
    return {"message": "Hello!"}

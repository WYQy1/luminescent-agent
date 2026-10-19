"""FastAPI 请求体与 Pydantic 字段校验练习。"""
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Stage 0 - Request Parameters")


class User(BaseModel):
    username: str = Field(
        min_length=2,
        max_length=10,
        description="用户名长度为 2 到 10 个字符",
    )
    password: str = Field(
        min_length=6,
        max_length=20,
        description="密码长度为 6 到 20 个字符",
    )


@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI!"}


@app.get("/book/{book_id}")
async def get_book(
    book_id: int = Path(..., gt=0, lt=101, description="书籍 ID 取值范围为 1 到 100")
):
    return {"id": book_id, "title": f"这是第 {book_id} 本书"}


@app.get("/news/news_list")
async def get_news_list(
    skip: int = Query(0, ge=0, description="跳过的条数"),
    limit: int = Query(10, gt=0, le=100, description="每页条数"),
):
    return {"skip": skip, "limit": limit}


@app.post("/register")
async def register(user: User):
    return {"username": user.username}

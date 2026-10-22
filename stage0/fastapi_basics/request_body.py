"""FastAPI 请求体与 Pydantic 字段校验练习。"""
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Stage 0 - Request Parameters")


class User(BaseModel):
    username: str = Field(
        min_length=2,
        max_length=10,
        description="用户名长度为 2 到 10 个字符",
        #tags: list[str] = []  #带类型参数的 List 字段  同理有tags: set[str] = set() 
        #dict[int, float]    
    )   

    password: str = Field(
        min_length=6,
        max_length=20,
        description="密码长度为 6 到 20 个字符",
    )
# class Image(BaseModel):
#     url: str
#     name: str

# image调用了Image模型 相当于大模型调用小模型
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     image: Image | None = None  或者 images: list[Image] setye'shi'o

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
    #新写法
    #from typing import Annotated
    #skip: Annotated[int, Query(ge=0, description="跳过条数")] = 0,
    #limit: Annotated[int, Query(le=100, description="每页条数")] = 10
): 
    return {"skip": skip, "limit": limit}
#好处:类型别名可以复用 
#PageSize = Annotated[int, Query(ge=1, le=100, description="每页条数")] Path Filed也适用

# @app.get("/users/")
# async def users(page: PageSize = 10): ...

# @app.get("/goods/")
# async def goods(page: PageSize = 20): ...

@app.post("/register")
async def register(user: User):
    return {"username": user.username,"pwd":user.password}

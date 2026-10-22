from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

#深层嵌套模型
class Image(BaseModel):
    url: HttpUrl   #定义为pydantic中的HttpUr类型 会自动检测是否是合法url地址
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
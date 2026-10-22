from datetime import datetime
from fastapi import FastAPI

#作用是把 Pydantic 模型（以及 datetime 这类特殊类型）转成可直接存入 JSON / 字典的普通 Python 数据
from fastapi.encoders import jsonable_encoder
#jsonable_encoder(item)：把模型对象转成普通字典
#item.model_dump() 作用和上边的相同 只适用于纯 Pydantic 模型
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
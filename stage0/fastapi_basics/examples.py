from pydantic import BaseModel,Field
#对应的 POST 接口请求体里自动填好这份示例，测试者点 "Try it out" 不用自己手敲字段，直接就能发请求。
#说白了就是给个测试样例不用在自己手动敲了
class Item1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2}
            ]
        }
    }
class Item2(BaseModel):
    name: str = Field(..., examples=["Foo"])  #Field适合单个字段
    price: float = Field(..., examples=[35.4])
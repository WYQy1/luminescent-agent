from fastapi import Depends,FastAPI,Query
from typing import Annotated
app = FastAPI(title="Stage 0 - FastAPI Basics")

@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI!"} 

#依赖注入 类比函数 将重复的代码包装起来 提高复用性
async def common_parammeters(
  skip:int=Query(0,ge=0),
  limit:int=Query(10,le=60)      
):
  return { "skip":skip,"limit":limit }
#写法1  common=Depends(common_parammeters)
#写法2  CommonsDep=Annotated[dict,Depends(common_parammeters)]  common:CommonsDep  提高复用性
CommonsDep=Annotated[dict,Depends(common_parammeters)]
@app.get("/news/new_list")
async def get_news(common:CommonsDep):
    return common

@app.get("/book/book_list")
async def get_news(common:CommonsDep):
    return common


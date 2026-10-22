from fastapi import FastAPI,HTTPException #HTTPException自定义相应异常
from fastapi.responses import HTMLResponse  #导入相应类型 本次类型为html  #JSONResponse 导入json类型
from fastapi.responses import FileResponse  #导入文件类型  
from pydantic import BaseModel #建立自定义返回类型
from pathlib import Path  #导入万能路径写法 换目录也不用改代码
app = FastAPI(title="Stage 0 - FastAPI Basics")


@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI!"}
#1.直接指定响应类型
@app.get("/html",response_class=HTMLResponse) #response_class=JSONResponse 返回json类型
async def get_html():
    return "<h1>这是一级标题</h1>"

#2.返回文件类型(通常为图片、音频等)
@app.get("/file")
async def get_file():
    #用r消除转义 或者用/ windows下都兼容
    image_path=Path(__file__).parent/"demo.jpg"  #相对路径的写法但是却是绝对路径的感觉
    return FileResponse(image_path,media_type="image/jpeg") #media_type表示返回类型 可以不写但写上更清楚

#3.自定义类型
class News(BaseModel):
    id:int
    title:str
    content:str

@app.get("/news/{id}",response_model=News)
async def get_news(id:int):
    return {
        "id":id,
        "title":f"这是第{id}本书",
        "content":"这本书是一本很不错的书"
    }
#4.异常处理
@app.get("/book/{id}")
async def get_book_id(id:int):
    id_list=[1,2,3,4,5,6]
    if id not in id_list:
        raise HTTPException(status_code=404,detail="您查询书本id不存在!",headers={"X-Error": "There goes my error"})
    return {"id":id}
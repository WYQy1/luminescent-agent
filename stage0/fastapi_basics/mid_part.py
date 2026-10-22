from fastapi import FastAPI,middleware  #导入中间件
from fastapi import Request #导入Request 是为了进行类型注解 为形参注解 加不加其实无所谓 加上更清楚
#中间件夹在客户端请求和路由函数之间，对每一个请求统一做一层预处理 / 后处理
#中间件对 app 里所有路由生效，不用在每个接口里重复写同一段逻辑。
import time
app = FastAPI(title="Stage 0 - FastAPI Basics")

#执行顺序是自下而上 谁的代码在下谁先执行 
# @app.middleware("/http")
# async def middleware1(request,call_back):
#     print("中间件1开始")
#     response=await call_back(request)
#     print("中间件1结束")
#     return response

# @app.middleware("http")
# async def middleware2(request,call_back):
#     print("中间件2开始")
#     response=await call_back(request)
#     print("中间件2结束")
#     return response


#补充一个小练习  计时器中间件
@app.middleware("http")
async def timer(request:Request,call_back):
    start=time.perf_counter()
    response=await call_back(request)
    cost=time.perf_counter()-start
    response.headers["X-Process-Time"] = str(cost)
    print(f"x-process-time:",{cost})  #显示在终端
    return response
@app.get("/")
async def read_root():
    start = time.perf_counter()
    cost = time.perf_counter() - start
    return {"message": "Hello FastAPI!","页面耗时":cost}  #显示在页面上

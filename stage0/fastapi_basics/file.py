from typing import Annotated
from fastapi import FastAPI,File,UploadFile,Form

app=FastAPI()

@app.post("/files/")
async def create_file(file:Annotated[bytes,File()]): #上传文件的类型是字节 File()告诉 FastAPI 这是一个从表单上传的文件。
    return {"file_size":len(file)}

#参数 file 是 UploadFile 对象，底层会流式读写临时文件（大文件更省内存）
#可通过 file.filename、file.content_type、file.file 等属性获取信息。
@app.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    return {"file_name":file.filename,"file_content_type":file.content_type,"file_file":file.file}



#File() 用于文件，Form() 用于文本  不用form标注会被当作查询参数
@app.post("/Files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()], #TypeError: object of type 'UploadFile' has no len()
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app.schemas.task import TaskCreate,TaskResponse,TaskUpdate
from app.crud.task import create_task,get_tasks,get_task_by_id,update_task,delete_task

router=APIRouter()
@router.post("/tasks",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task_in:TaskCreate,db:Session=Depends(get_db)):
    return create_task(db,task_in)

# // response_model=list[TaskResponse] → 一个 JSON 数组
# [
#   {"id": 1, "title": "写代码", "status": "pending", ...},
#   {"id": 2, "title": "买菜",   "status": "done",    ...}
@router.get("/tasks",response_model=list[TaskResponse])  
def get_task_endpoint(db:Session=Depends(get_db)):
    return get_tasks(db)
@router.get("/tasks/{task_id}")
def get_task_by_id_endpoint(task_id:int,db:Session=Depends(get_db)):
    task=get_task_by_id(db,task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return task
@router.patch("/tasks/{task_id}",response_model=TaskResponse)
def  update_task_endpoint(task_id:int,task_in:TaskUpdate,db:Session=Depends(get_db)):
    task=update_task(db,task_id,task_in)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    return task
@router.delete("/tasks/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task_endpoint(task_id:int,db:Session=Depends(get_db)):
    task=delete_task(db,task_id)
    if task is None:
       raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
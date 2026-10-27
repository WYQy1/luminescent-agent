from app.models import Task
from app.schemas.task import TaskCreate,TaskUpdate
from sqlalchemy.orm import Session
from sqlalchemy import select

def create_task(db:Session,task_in:TaskCreate):
        db_task=Task(title=task_in.title,description=task_in.description,status="pending")
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

def get_tasks(db:Session):
        tasks=db.scalars(select(Task)).all()
        return tasks
def get_task_by_id(db:Session,task_id:int):
        stmt=select(Task).where(Task.id==task_id)
        task=db.scalars(stmt).first()
        return task
# PATCH 的语义是 "只传要改的字段"
def update_task(db:Session,task_id:int,task_in:TaskUpdate):
        stmt=select(Task).where(Task.id==task_id)
        task = db.scalars(stmt).first()
        if task is None:
             return None          # exclude_unset=True 只保留客户端真的传过来的字段，没传的字段不放进字典
        update_data =task_in.model_dump(exclude_unset=True)  #把Pydantic模型对象转成一个普通 Python dict
        for field,value in update_data.items():
            #setattr(task, "title", "新标题") # 等价于task.title = "新标题"
            setattr(task,field,value)    #等价于task.field = value
            #客户端传入的数据:
            #PATCH /tasks/1
            #{"title": "新标题", "status": "done"}
            #update_data = {"title": "新标题", "status": "done"}
            #等价于：# task.title = "新标题" # task.status = "done" # description 没传，保持原样
        db.commit()
        db.refresh(task)
        return task
def delete_task(db:Session,task_id:int):
      stmt=select(Task).where(Task.id==task_id)
      task = db.scalars(stmt).first()
      if task is None:
             return None
      db.delete(task)
      db.commit()
      return task

                      


from app.database import SessionLocal
from app.models import Task
from sqlalchemy import select

with SessionLocal() as session:
    tasks=session.scalars(select(Task)).all()
    for task in tasks:
        print(task.id,task.title,task.status)
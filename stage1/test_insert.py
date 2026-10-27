from app.database import SessionLocal
from app.models import Task

with SessionLocal() as session:
        stmt=Task(title="学习 SQLAlchemy",description="完成第一条数据库插入测试",status="pending")
        session.add(stmt)
        session.commit()
        print(stmt.id)
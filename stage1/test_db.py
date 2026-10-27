from app.database import engine,Base
from app.models import Task


Base.metadata.create_all(bind=engine)
print("建表操作执行完成")
    
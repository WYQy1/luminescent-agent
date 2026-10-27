from sqlalchemy import select,func
from main import SessionLocal
from models import User

with SessionLocal() as session:
    stmt1=select(User).order_by(User.age.asc()) #升序  .desc()降序
    users1=session.scalars(stmt1).all()
    for u in users1:
        print(u.age)

    stmt2=select(User).order_by(User.id).offset(3).limit(4) #offset:跳过几条 limit:取几条
    users2=session.scalars(stmt2).all()
    for u in users2:
        print(u.name,u.age)

    stmt3=select(func.count()).select_from(User)  #func.count()统计有几行
    total=session.scalar(stmt3)
    print("用户总数",total)

    stmt4 = select(func.sum(User.age))  #func.sum()统计总和
    total = session.scalar(stmt4)
    print("用户总年龄", total)
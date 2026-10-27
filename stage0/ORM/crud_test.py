from main import SessionLocal
from sqlalchemy import select
from models import User
#练习2
# with SessionLocal() as session:
#     users = [
#         User(name="Tom", age=18,email="00000"),
#         User(name="Amy", age=22,email="00000"),
#         User(name="Jack", age=30,email="00000"),
#     ]
#     session.add_all(users)
#     session.commit()

#     for u in users:
#         session.refresh(u)
#         print(f"新增用户 id={u.id}, name={u.name}, age={u.age}")

#练习3
with SessionLocal() as session:
    stmt=select(User).where(User.age>=20)
    users=session.scalars(stmt).all()
    for user in users:
        print(user.id,user.name,user.age)
#练习4
with SessionLocal() as session:
    stmt=select(User).order_by(User.age.desc())
    users=session.scalars(stmt).all()
    for user in users:
        print(user.id,user.name,user.age)
#练习5
with SessionLocal() as session:
     stmt=select(User).where(User.id==2)
     users=session.scalars(stmt).first()
     if user is None:
          print("没有找到该用户")
     print(user.id,user.name,user.age)
#练习6
with SessionLocal() as session:
    user=session.get(User,2)
    if user is None:
        print("未找到")
    else:
        user.age=28
        session.commit()
        print("修改完成！")
        print(user.age)

#练习7
with SessionLocal() as session:
     user=session.get(User,3)
     if user is None:
             print("未找到")
     else:
        session.delete(user)
        session.commit()
        print("删除成功！")
     

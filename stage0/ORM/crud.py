from sqlalchemy import select
from main import SessionLocal
from models import User
#1.create
# with SessionLocal() as session:
#     user=User(name="wyq",age=24)
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     print(f"新增用户id是{user.name},年龄为{user.age}")

#2.1read all
# with SessionLocal() as session:
#     stmt=select(User)
#     users=session.scalars(stmt).all()
#     for user in users:
#         print(user.id,user.name,user.age)

#2.2 read alone(按照id/age等)
# target_id=1
# with SessionLocal() as session:
#      stmt=select(User).where(User.id==target_id)
#      user=session.scalars(stmt).first()
#      if user is None:
#           print("没有找到该用户")
#      print(user.id,user.name,user.age)

#3.update
# target_id=1
# with SessionLocal() as session:
#     user=session.get(User,target_id)
#     if user is None:
#         print("没有找到这个用户")
#     else:
#         user.age=26
#         session.commit()
#         print("修改完成！")

#4.delete
# target_id=1
# with SessionLocal() as session:
#      user=session.get(User,target_id)
#      if user is None:
#          print("没有找到这个用户")
#      else:
#          session.delete(user)
#          session.commit()
#          print("删除完成！")
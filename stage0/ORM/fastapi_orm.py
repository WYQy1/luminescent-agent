from fastapi import FastAPI,HTTPException
from sqlalchemy import select
from main import SessionLocal
from models import User

app=FastAPI()

@app.post("/users")
def create_user(name:str,age:int,email:str):
    with SessionLocal() as session:
        user=User(name=name,age=age,email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"id":user.id,"name":user.name,"age":user.age}

@app.get("/users")
def list_users():
     with SessionLocal() as session:
         users=session.scalars(select(User)).all()
     return [{"id": u.id, "name": u.name, "age": u.age} for u in users]

@app.get("/users/{user_id}")
def get_user(user_id:int):
     with SessionLocal() as session:
         user=session.get(User,user_id)
         if user is None:
            raise HTTPException(status_code=404,detail="User not found")
         return {"id":user.id,"name":user.name,"age":user.age}

@app.put("/users/{user_id}")
def update_user(user_id:int,age:int):
     with SessionLocal() as session:
         user=session.get(User,user_id)
         if user is None:
            raise HTTPException(status_code=404,detail="User not found")
         user.age=age
         session.commit()
         return {"id":user.id,"name":user.name,"age":user.age}

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
     with SessionLocal() as session:
             user=session.get(User,user_id)
             if user is None:
                raise HTTPException(status_code=404,detail="User not found")
             session.delete(user)
             session.commit()
             return {"message":"deleted","id":user.id}
from pydantic import BaseModel,ConfigDict
from datetime import datetime
class TaskCreate(BaseModel):
      title:str
      description:str
class TaskUpdate(BaseModel):
      title: str | None = None
      description: str | None = None
      status: str | None = None

class TaskResponse(BaseModel):
      id:int
      title:str
      description:str
      status:str
      created_time:datetime
      model_config = ConfigDict(from_attributes=True)
               
    
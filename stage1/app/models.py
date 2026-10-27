from app.database import Base
from datetime import datetime
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import DateTime,String
class Task(Base):
    __tablename__="tasks"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    status:Mapped[str]=mapped_column(String(1000),nullable=False)
    created_time: Mapped[datetime] = mapped_column(DateTime,default=datetime.now,nullable=False)

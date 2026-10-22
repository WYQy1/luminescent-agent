from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql://root:wyq123456..@localhost:3306/fastapi_demo",
    echo=True, #执行的具体操作会展示出来
)
SessionLocal = sessionmaker(bind=engine)
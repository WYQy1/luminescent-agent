from main import engine
from models import Base
Base.metadata.create_all(bind=engine)  #指定用哪个数据库连接去建表，也就是 main.py 里那个 create_engine(...)。
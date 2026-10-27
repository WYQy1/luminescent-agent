from sqlalchemy.engine import URL
from app.core.config import settings
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.models import Task
import pytest
client=TestClient(app)

#    测试目标	      是否需要先创建	              原因
# 查询不存在的任务	    不需要	           直接查询一个确认不存在的 ID
# 更新不存在的任务	    不需要	           直接更新一个确认不存在的 ID
# 创建任务	           不需要	           创建本身就是测试目标
# 查询刚创建的任务	    需要	           要验证创建后的记录能否查询
# 更新已有任务	        需要	           要验证已存在的记录能否修改
# 删除已有任务	        需要	           要验证真实记录能否删除
def test_hello():
    response= client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_task():
    payload = {
    "title": "自动化测试任务",
    "description": "验证创建任务接口"
       }
    response = client.post("/tasks", json=payload)
    data=response.json()
    assert response.status_code==201
    assert data["title"]==payload["title"] and data["description"]==payload["description"]
    assert data["status"]=="pending"
    assert "id" in data
    assert "created_time" in data
    db = TestingSessionLocal()
    try:
        task=db.get(Task,data["id"])
        assert task is not None
        assert task.title==payload["title"]
    finally:
       db.close()
#先tasks 后tasks/id 是正常的测试流程 能保证前者正常运行后在测试id才有意义
#了让 GET 测试有一个确定存在、数据已知的 id 可查
def test_get_task_by_id():
     payload={ "title": "自动化测试任务","description": "验证创建任务接口"}
     response= client.post("/tasks",json=payload)
     create_data=response.json()
     get_response=client.get(f"/tasks/{create_data['id']}")
     task=get_response.json()
     assert response.status_code==201
     assert get_response.status_code==200
     assert create_data["title"]==task["title"]
     assert create_data["id"]==task["id"]
     
def test_get_task_not_found():
    response=client.get("/tasks/999999")
    assert response.status_code==404

def test_update_task():
    payload={ "title": "自动化测试任务","description": "验证创建任务接口"}
    response= client.post("/tasks",json=payload)
    data=response.json()
    update_payload = {"title": "自动化测试"}
    res=client.patch(f"/tasks/{data['id']}",json=update_payload)
    assert res.status_code==200
    assert res.json()["title"] == "自动化测试"
    db = TestingSessionLocal()
    try:
        task=db.get(Task,data["id"])
        assert task is not None
        assert task.title=="自动化测试"
    finally:
        db.close()

def test_update_task_not_found():
    update_payload = {"title": "自动化测试"}
    response=client.patch("/tasks/999999",json=update_payload)
    assert response.status_code==404   

def test_delete_task():
    payload={ "title": "自动化测试任务","description": "验证创建任务接口"}
    response=client.post("/tasks",json=payload)
    task=response.json()
    get_response=client.delete(f"/tasks/{task['id']}")
    assert get_response.status_code==204
    res=client.get(f"/tasks/{task['id']}")
    assert res.status_code==404
    
TEST_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database="task_knowledge_test_db",
)
test_engine=create_engine(TEST_DATABASE_URL)
TestingSessionLocal=sessionmaker(bind=test_engine)
Base.metadata.create_all(bind=test_engine)
def override_get_db():
    db=TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
@pytest.fixture(autouse=True)
def clean_test_data():
    db = TestingSessionLocal()
    try:
        db.query(Task).delete()
        db.commit()

        yield db

        db.query(Task).delete()
        db.commit()
    finally:
        db.close()
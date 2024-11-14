from fastapi.testclient import TestClient
from main import app
from .users.models import Base
from database import engine, SessionLocal

client = TestClient(app)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[SessionLocal] = override_get_db

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_user():
    response = client.post("/users/", json={"name": "Jane Doe", "email": "jane@example.com"})
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane@example.com"

def test_read_user_error():
    user_id = "10"
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404
    
def test_update_user():
    response = client.post("/users/", json={"name": "John Smith", "email": "johnsmith@example.com"})
    user_id = response.json()["id"]
    response = client.put(f"/users/{user_id}", json={"name": "John Updated", "email": "johnupdated@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Updated"
    assert response.json()["email"] == "johnupdated@example.com"

def test_update_user_error():
    user_id = 10
    response = client.put(f"/users/{user_id}", json={"name": "None Updated", "email": "noneupdated@example.com"})
    assert response.status_code == 404

def test_delete_user():
    response = client.post("/users/", json={"name": "Jane Smith", "email": "janesmith@example.com"})
    user_id = response.json()["id"]
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "User deleted"

def test_delete_user_error():
    user_id = "10"
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 404

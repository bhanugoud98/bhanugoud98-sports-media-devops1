# user-service/tests/test_app.py
import json
import pytest
from multiprocessing import Process
import time
import requests
import app as user_app

BASE_URL = "http://127.0.0.1:5001"

@pytest.fixture(scope="module", autouse=True)
def start_server():
    proc = Process(target=user_app.app.run, kwargs={"host":"127.0.0.1", "port":5001})
    proc.start()
    time.sleep(1)
    yield
    proc.terminate()
    proc.join()

def test_health():
    r = requests.get(f"{BASE_URL}/api/health")
    assert r.status_code == 200
    body = r.json()
    assert body.get("status") == "ok"

def test_create_and_get_user():
    payload = {"email": "test@example.com", "name": "John"}
    r = requests.post(f"{BASE_URL}/api/users", json=payload)
    assert r.status_code == 201
    user = r.json()
    uid = user["id"]
    # retrieve
    r2 = requests.get(f"{BASE_URL}/api/users/{uid}")
    assert r2.status_code == 200
    assert r2.json()["email"] == "test@example.com"

def test_list_users():
    r = requests.get(f"{BASE_URL}/api/users")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

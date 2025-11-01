# order-service/tests/test_app.py
import json
import pytest
from multiprocessing import Process
import time
import requests
import app as order_app

BASE_URL = "http://127.0.0.1:5002"

@pytest.fixture(scope="module", autouse=True)
def start_server():
    proc = Process(target=order_app.app.run, kwargs={"host":"127.0.0.1", "port":5002})
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

def test_create_and_get_order():
    payload = {"user_id": "u123", "product_ids": ["p1", "p2"]}
    r = requests.post(f"{BASE_URL}/api/orders", json=payload)
    assert r.status_code == 201
    order = r.json()
    oid = order["id"]
    # retrieve
    r2 = requests.get(f"{BASE_URL}/api/orders/{oid}")
    assert r2.status_code == 200
    assert r2.json()["user_id"] == "u123"

def test_list_orders():
    r = requests.get(f"{BASE_URL}/api/orders")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

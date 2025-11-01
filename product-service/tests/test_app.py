# product-service/tests/test_app.py
import json
import pytest
from multiprocessing import Process
import time
import requests
import app as product_app

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture(scope="module", autouse=True)
def start_server():
    # start flask app in a process
    proc = Process(target=product_app.app.run, kwargs={"host":"127.0.0.1", "port":5000})
    proc.start()
    time.sleep(1)  # wait for server to start
    yield
    proc.terminate()
    proc.join()

def test_health():
    r = requests.get(f"{BASE_URL}/api/health")
    assert r.status_code == 200
    body = r.json()
    assert body.get("status") == "ok"

def test_create_and_get_product():
    payload = {"name": "Test Product", "price": 9.99}
    r = requests.post(f"{BASE_URL}/api/products", json=payload)
    assert r.status_code == 201
    product = r.json()
    pid = product["id"]
    # retrieve
    r2 = requests.get(f"{BASE_URL}/api/products/{pid}")
    assert r2.status_code == 200
    assert r2.json()["name"] == "Test Product"

def test_list_products():
    r = requests.get(f"{BASE_URL}/api/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

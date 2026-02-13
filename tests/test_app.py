import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_products():
    client = app.test_client()
    res = client.get("/products")
    assert res.status_code == 200
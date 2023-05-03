import json

from app import app

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'WORKING'

def test_get_all_products():
    response = app.test_client().get('/products')

    res = json.loads(response.data.decode('utf-8')).get("data")
    assert len(res) == 0
    assert response.status_code == 200
    assert type(res) is list

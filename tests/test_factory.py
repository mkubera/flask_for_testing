from flaskr import create_app, sum_aod
from flask import json

def test_config():
	assert not create_app().testing
	assert create_app({'TESTING': True}).testing

def test_root(client):
	resp = client.get('/')

	assert resp.data == b"Hi, I'm the ROOT of the app"

def test_api_get_strategists(client):
	resp = client.get('/api/v1/strategists')
	data = json.loads(resp.data)

	assert data['data'][0] == {"id": 1, "name": "Hannibal", "aod": 69}
	assert data['aod_total'] == 177
	
def test_sum_aod():
	strategists = [{'aod': 1},{'aod': 2},{'aod': 3}]
	total = sum_aod(strategists)

	assert total == 6
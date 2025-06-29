import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

def test_message():
    with app.test_client() as client:
        response = client.get('/api/message')
        assert response.status_code == 200
        data = response.get_json()
        assert 'message' in data
        assert data['message'].startswith('Hello from Flask')

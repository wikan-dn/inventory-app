import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

def test_ping_route():
    with app.test_client() as client:
        response = client.get('/ping')
        assert response.status_code == 200
        assert response.json == {"message": "pong"}

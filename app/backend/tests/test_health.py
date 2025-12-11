import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    """Test the health check endpoint."""
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.json == {"status": "healthy"}

def test_health_live(client):
    """Test the liveness probe."""
    rv = client.get('/health/live')
    assert rv.status_code == 200
    assert rv.json == {"status": "alive"}

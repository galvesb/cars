import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_obtain_token(client):
    response = client.post('/token/', {'username': 'user', 'password': 'password'})
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

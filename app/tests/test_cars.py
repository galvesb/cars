import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_create_car(client, access_token):
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = client.post('/cars/', {'model': 'Tesla Model S', 'owner': 1})
    assert response.status_code == 201
    assert response.data['model'] == 'Tesla Model S'

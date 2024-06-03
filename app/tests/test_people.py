import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_create_person(client):
    response = client.post('/people/', {'name': 'John Doe', 'age': 30})
    assert response.status_code == 201
    assert response.data['name'] == 'John Doe'

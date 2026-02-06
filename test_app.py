import pytest
from app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
<<<<<<< HEAD
    expected_text = 'Sudhanshu'
=======
    expected_text = 'juwaira faiza'
    expected_text = 'Faiza'
>>>>>>> 52fe92828cd7d6ef2a23565659465c739ec8b743
    assert expected_text.encode() in response.data

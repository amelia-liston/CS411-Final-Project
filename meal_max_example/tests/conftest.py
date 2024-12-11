import pytest

from app import create_app
from config import TestConfig
from meal_max.db import db

@pytest.fixture
def app():
    app = create_app(TestConfig)
    app.config['ACCESS_TOKEN'] = "test_access_token"
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def session(app):
    with app.app_context():
        yield db.session

@pytest.fixture
def access_token(app):
    """Fixture to return the access token."""
    return app.config['ACCESS_TOKEN']

@pytest.fixture
def authenticated_client(client, access_token):
    """Fixture to return a client with authentication headers."""
    client.environ_base['HTTP_AUTHORIZATION'] = f"Bearer {access_token}"
    return client
import pytest

from app import create_app


def test_config():
    assert create_app({"TESTING": True}).testing


@pytest.fixture
def app():
    app = create_app("TEST")
    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

import pytest
from django.test import Client


@pytest.mark.django_db
def test_hello_world():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello World" in response.content

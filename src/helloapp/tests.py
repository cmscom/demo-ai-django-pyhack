from datetime import timedelta

import pytest
from django.test import Client
from django.utils import timezone

from .models import Application, Event


@pytest.mark.django_db
def test_hello_world():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello World" in response.content


@pytest.mark.django_db
def test_create_event():
    start = timezone.now()
    end = start + timedelta(days=1)
    event = Event.objects.create(
        title="PyHack Conference",
        start_date=start,
        end_date=end,
        capacity=100,
        description="PyHackに関するイベントです。"
    )
    assert Event.objects.count() == 1
    assert event.title == "PyHack Conference"
    assert event.capacity == 100


@pytest.mark.django_db
def test_create_event_and_application():
    start = timezone.now()
    end = start + timedelta(days=1)
    event = Event.objects.create(
        title="PyHack Conference",
        start_date=start,
        end_date=end,
        capacity=100,
        description="PyHackに関するイベントです。"
    )

    application = Application.objects.create(
        event=event,
        applicant_name="テストユーザー",
        applicant_email="test@example.com"
    )

    assert Event.objects.count() == 1
    assert Application.objects.count() == 1
    assert application.event == event
    assert application.applicant_name == "テストユーザー"
    assert application.applicant_email == "test@example.com"

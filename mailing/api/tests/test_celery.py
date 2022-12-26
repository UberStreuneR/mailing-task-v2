from api.tasks import designate_messages, run_mailings, create_message, send_message
from api.models import Message, Client, Mailing
from django.db import transaction
import pytest
from os import getenv


@pytest.mark.django_db(transaction=True)
@pytest.mark.celery(result_backend=getenv("CELERY_BACKEND"))
class TestTasks:

    def test_request(self):
        try:
            send_message.delay(3, "79150001234", "some message")
        except Exception as e:
            assert False

    def test_wrong_request(self):
        try:
            send_message.delay(3, "7", "some message")
            assert False
        except Exception as e:
            assert True

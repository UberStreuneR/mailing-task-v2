import pytest
from api.serializers import ClientSerializer, MailingSerializer, MessageSerializer
from django.utils import timezone
from datetime import timedelta


@pytest.mark.django_db
@pytest.fixture
def client_serializer():
    data = {
        "phone_number": "79150001234",
        "tag": "some_tag"
    }
    client = ClientSerializer(data=data)
    assert client.is_valid()
    client.save()
    return client


@pytest.mark.django_db
@pytest.fixture
def mailing_serializer():
    data = {
        "start_time": timezone.now() - timedelta(minutes=5),
        "end_time": timezone.now() + timedelta(minutes=5),
        "message_text": "Hello world",
        "client_filter": "tag"
    }
    mailing = MailingSerializer(data=data)
    assert mailing.is_valid()
    mailing.save()
    return mailing


@pytest.mark.django_db
@pytest.fixture
def message_serializer(client_serializer, mailing_serializer):
    data = {
        "mailing": mailing_serializer.data['id'],
        "client": client_serializer.data['id'],
    }
    message = MessageSerializer(data=data)
    assert message.is_valid()
    message.save()
    return message

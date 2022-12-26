from api.serializers import ClientSerializer, MessageSerializer, MailingSerializer
from api.models import Client, Mailing, Message
from api.utils import get_all_clients_by_filter
import pytest
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone


@pytest.mark.django_db
def test_clients():
    data = {
        "phone_number": "79150001234",
        "tag": "some_tag"
    }

    client = ClientSerializer(data=data)
    assert client.is_valid()
    client.create(client.validated_data)
    assert Client.objects.count() == 1

    client2 = ClientSerializer(
        data=data.update({"phone_number": "89150001234"}))
    assert not client2.is_valid()

    client3 = ClientSerializer(
        data=data.update({"phone_number": "791500012345"}))
    assert not client3.is_valid()


@pytest.mark.django_db
def test_clients_search():
    data = {
        "phone_number": "79000000000",
        "tag": "some_tag"
    }
    client = ClientSerializer(data=data)
    assert client.is_valid()
    client.save()

    clients = get_all_clients_by_filter("900")
    assert len(clients) == 1

    clients = get_all_clients_by_filter("some_tag")
    assert len(clients) == 1


@pytest.mark.django_db
def test_mailings(client_serializer, mailing_serializer, message_serializer):
    # def test_mailings(client_serializer):
    assert client_serializer.data['phone_number'] == "79150001234"
    assert mailing_serializer.data['message_text'] == "Hello world"
    assert message_serializer.data['client'] == client_serializer.data['id']
    assert message_serializer.data['mailing'] == mailing_serializer.data['id']

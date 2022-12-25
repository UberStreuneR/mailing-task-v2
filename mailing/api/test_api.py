from api.serializers import ClientSerializer
from api.models import Client, Mailing, Message
import pytest


@pytest.mark.django_db
def test_clients():
    data = {
        "phone_number": "79164756389",
        "tag": "rofl"
    }

    client = ClientSerializer(data=data)
    assert client.is_valid()
    client.create(client.validated_data)
    assert Client.objects.count() == 1

    client2 = ClientSerializer(
        data=data.update({"phone_number": "89164756389"}))
    assert not client2.is_valid()

    client3 = ClientSerializer(
        data=data.update({"phone_number": "791647563890"}))
    assert not client3.is_valid()

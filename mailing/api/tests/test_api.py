import pytest


@pytest.mark.django_db
def test_clients(client, client_serializer):
    response = client.get("/api/clients/")
    assert response.json()[0] == client_serializer.data


@pytest.mark.django_db
def test_mailings(client, mailing_serializer):
    response = client.get("/api/mailings/")
    assert response.json()[0] == mailing_serializer.data


@pytest.mark.django_db
def test_messages(client, message_serializer):
    response = client.get("/api/messages/")
    assert response.json()[0] == message_serializer.data

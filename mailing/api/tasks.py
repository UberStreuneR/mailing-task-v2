from mailing.celery import app
from api.models import Mailing, Client, Message
from api.serializers import MailingSerializer
from api.utils import get_all_clients_by_filter
from api.exceptions import UnauthorizedException
from api.task_classes import MessageTask
from datetime import datetime
from django.utils import timezone
from celery.utils.log import get_task_logger
from os import getenv
import requests


logger = get_task_logger(__name__)


@app.task
def designate_messages(id: int):
    mailing = Mailing.objects.get(pk=id)
    if mailing.start_time < timezone.now():
        if mailing.end_time > timezone.now():
            serializer = MailingSerializer(mailing)
            logger.info(f"Serializer data: {serializer.data}")
            run_mailings.delay(serializer.data)
    return mailing.start_time, mailing.end_time, timezone.now()


@app.task
def run_mailings(serialized_mailing: dict):
    clients = get_all_clients_by_filter(serialized_mailing['client_filter'])
    for client in clients:
        create_message.delay(
            serialized_mailing['id'], serialized_mailing['message_text'], client.id, client.phone_number)


@app.task
def create_message(mailing_id: int, mailing_message: str, client_id: int, client_phone: str):
    message = Message(mailing_id=mailing_id, client_id=client_id)
    message.save()
    send_message.delay(message.id, client_phone, mailing_message)
    return message


@app.task(bind=True, base=MessageTask, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={'max_retries': 5})
def send_message(self, id: int, phone: str, text: str):
    headers = {"Authorization": f"Bearer {getenv('API_TOKEN')}"}
    json = {"id": id, "phone": phone, "text": text}
    url = getenv("API_URL") + str(id)
    res = requests.post(url, json=json, headers=headers)
    if res.status_code != 200:
        if res.status_code == 401:
            logger.error("Authorization failed")
            raise UnauthorizedException()
        msg = f"Request to send a message was not successful ({res.status_code})"
        logger.error(msg)
        raise Exception(msg)
    logger.info("Request successful")

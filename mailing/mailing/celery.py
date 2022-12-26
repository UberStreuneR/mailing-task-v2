from celery import Celery
from kombu import Queue, Exchange
from os import getenv

app = Celery("mailing", broker=getenv("CELERY_BROKER"),
             backend=getenv("CELERY_BACKEND"))
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf.task_queues = (
    Queue("mailing", Exchange('mailing', type="topic",
          auto_delete=True), routing_key="mailing.*"),
)
app.conf.task_routes = {
    "api.tasks.*": {"exchange": "mailing", "routing_key": "mailing.tasks"}
}

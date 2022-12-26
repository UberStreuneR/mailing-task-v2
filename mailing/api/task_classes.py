from mailing.celery import app
from api.models import Message
from celery.utils.log import logger


class MessageTask(app.Task):
    def before_start(self, task_id, args, kwargs):
        message_id = args[0]
        self.message = Message.objects.get(pk=message_id)
        self.message.status = "P"
        self.message.save()
        return super().before_start(task_id, args, kwargs)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        return super().after_return(status, retval, task_id, args, kwargs, einfo)

    def on_success(self, retval, task_id, args, kwargs):
        self.message.status = "S"
        self.message.save()
        return super().on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.message.status = "E"
        self.message.save()
        return super().on_failure(exc, task_id, args, kwargs, einfo)

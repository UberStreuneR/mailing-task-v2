from django.db import models
import pytz
from django.utils import timezone

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
MESSAGE_STATUSES = (
    ('S', 'Sent'),
    ('P', 'Pending'),
    ('E', 'Error'),
    ('U', 'Uninitiated')
)


class Mailing(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message_text = models.TextField()
    client_filter = models.CharField(max_length=5)


class Client(models.Model):
    phone_number = models.CharField(max_length=11)
    mobile_operator = models.CharField(max_length=3, blank=True)
    tag = models.CharField(max_length=10, blank=True)
    timezone = models.CharField(
        max_length=32, choices=TIMEZONES, default='Europe/Moscow')

    def __str__(self) -> str:
        return f"{self.phone_number}, {self.timezone}, id {self.id}"


class Message(models.Model):
    sent_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=1, choices=MESSAGE_STATUSES, default='U')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

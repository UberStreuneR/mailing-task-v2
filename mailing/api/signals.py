from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from api.models import Mailing
from api.tasks import designate_messages


@receiver(post_save, sender=Mailing)
def create_mailing_message_tasks(sender, instance, created, *args, **kwargs):
    if created:
        transaction.on_commit(lambda: designate_messages.delay(instance.id))

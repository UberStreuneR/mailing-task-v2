from django.db.models import Q
from api.models import Client


def get_all_clients_by_filter(filter_: str):
    return Client.objects.filter(Q(tag__contains=filter_) | Q(mobile_operator__contains=filter_))

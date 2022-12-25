from django.urls import path
from api import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'mailings', views.MailingViewSet)
urlpatterns = router.urls

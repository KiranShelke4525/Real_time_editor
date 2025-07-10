from django.urls import re_path
from backend_app.consumers import DocumentConsumer

websocket_urlpatterns = [
    re_path(r"ws/document/$", DocumentConsumer.as_asgi()),
]

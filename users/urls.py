from django.contrib import admin
from django.urls import path, include
from .views import ListSubscribedEvents, ListMyEvents, UpdateMyEvents


urlpatterns = [
    path(
        "subscribed_events/", ListSubscribedEvents.as_view(), name="subscribed_events"
    ),
    path("my_events/", ListMyEvents.as_view(), name="my_events"),
    path("my_events/<int:pk>", UpdateMyEvents.as_view(), name="update_event"),
]

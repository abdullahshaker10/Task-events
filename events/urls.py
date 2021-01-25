from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("", ListEvents.as_view(), name="events"),
    path("events/<int:pk>", EventDetail.as_view(), name="event_detail"),
    path("events/", CreateEvents.as_view(), name="create_event"),
    path("api/events/<int:pk>", AddParticipant.as_view(), name="add_participant"),
    path("api/my_events/<int:pk>", WithdrawEvents.as_view(), name="withdraw_event"),
]

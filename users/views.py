from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from events.models import Event


class UpdateMyEvents(UpdateView):
    model = Event
    fields = ["title", "description", "date"]
    template_name_suffix = "_update_form"


class ListSubscribedEvents(LoginRequiredMixin, ListView):
    context_object_name = "subscribed_events"
    template_name = "events/subscribed_events_list.html"
    paginate_by = 6

    def get_queryset(self):
        return self.request.user.events.all()


class ListMyEvents(LoginRequiredMixin, ListView):
    context_object_name = "my_events"
    template_name = "events/my_events_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user)

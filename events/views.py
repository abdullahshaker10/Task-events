from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Event
from rest_framework.generics import UpdateAPIView
from .serializers import EventSerializer, CustomUserSerializer
from .forms import EventForm
from .mixins import EventMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CreateEvents(LoginRequiredMixin, CreateView):
    form_class = EventForm
    template_name = "events/events_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateEvents, self).form_valid(form)


class ListEvents(EventMixin, ListView):
    context_object_name = "events"
    template_name = "events/events_list.html"
    paginate_by = 6


class EventDetail(DetailView):
    model = Event
    template_name = "events/event_detail.html"


class AddParticipant(LoginRequiredMixin, UpdateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class WithdrawEvents(LoginRequiredMixin, UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

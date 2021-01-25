from .models import Event


class EventMixin:
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.exclude(participant=self.request.user).all()
        return Event.objects.all()

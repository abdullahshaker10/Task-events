from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

CustomUser = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    owner = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name="events_owner"
    )
    participant = models.ManyToManyField(
        CustomUser, related_name="events", blank=True)

    def __str__(self):
        return self.title

    @property
    def praticipents_numbers(self):
        return self.participant.count

    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.id)])

    class Meta:
        ordering = ("date",)
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]

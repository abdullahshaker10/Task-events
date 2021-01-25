from rest_framework import serializers
from .models import Event
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def update(self, instance, validated_data):
        body = self.context["request"].data
        event_id = body["id"]
        event = Event.objects.get(id=event_id)
        instance.events.remove(event)
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def update(self, instance, validated_data):
        participent = self.context["request"].user
        instance.participant.add(participent)
        instance.save()
        return instance

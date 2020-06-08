from rest_framework import serializers

from . import models
from scheduler_api.models import Scheduler


class AddUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'email',
            'user_category',
            'available_date',
            'available_time_from',
            'available_time_to'
        )


class SchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = '__all__'

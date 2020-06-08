from rest_framework import serializers

from . import models
from scheduler_api.models import Scheduler


class UserScheduleSerializer(serializers.ModelSerializer):
    time_slots = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = (
            'email',
            'user_category',
            'available_date',
            'time_slots'
        )

    def get_time_slots(self, obj):
        data_obj = Scheduler.objects.filter(user__id=obj.id)
        data_ser = SchedulerListSerializer(data_obj, many=True)
        time_slot = [x['time_slot'] for x in data_ser.data]
        return time_slot


class SchedulerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheduler
        fields = ('time_slot',)

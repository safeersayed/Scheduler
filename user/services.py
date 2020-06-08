"""
# Service file for user app.
# Business logic will written on this file.
"""
import datetime

from rest_framework import status
from rest_framework.response import Response

from . import serializers


class UserManagementServices:

    def register_user(self, data):
        """
        Register a new user
        :param data: include user info and available time period as 24hr format
        :return: status and user info
        """
        serializer = serializers.AddUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_obj = serializer.save()
            # create the slots
            self.create_time_slots(user=user_obj.id,
                                   start_time=user_obj.available_time_from,
                                   end_time=user_obj.available_time_to
                                   )
            return Response(
                {
                    'status': 201,
                    'message': 'New post added successfully',
                    'data': serializers.AddUserSerializer(user_obj).data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'status': 400,
                    'message': 'Something went wrong',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def create_time_slots(self, user, start_time, end_time, slot_time=60):
        """
        create available time into 1hr slots
        :param user: user id
        :param start_time: time that user available from [24 hr]
        :param end_time: time that user available to [24 hr]
        :param slot_time: time duration[in mins]
        :return: None
        """
        time_slots = []
        time = datetime.datetime.strptime(start_time, '%H:%M')
        end = datetime.datetime.strptime(end_time, '%H:%M')
        while time <= end:
            pre_time = time
            time += datetime.timedelta(minutes=slot_time)
            time_interval = str(pre_time.strftime("%H:%M")) + "-" + str(time.strftime("%H:%M"))
            # check the start time and end time are same
            if time <= end:
                scheduler_obj = {'user': user, 'time_slot': time_interval}
                time_slots.append(scheduler_obj)

        scheduler_ser = serializers.SchedulerSerializer(data=time_slots, many=True)
        if scheduler_ser.is_valid(raise_exception=True):
            scheduler_ser.save()
        return

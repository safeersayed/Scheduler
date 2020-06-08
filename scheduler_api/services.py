# service file for scheduler_api app
from rest_framework import status
from rest_framework.response import Response

from . import models
from . import serializers


class SchedulerService:

    def schedule_list(self, interviewer_id, candidate_id):
        """
        Get the schedule list based on inputs
        :param interviewer_id: interviewer email
        :param candidate_id: candidate email
        :return: time-slots as list
        """
        interviewer_details = candidate_details = []
        if interviewer_id:
            interviewer_details = self.get_data(email_id=interviewer_id)
        if candidate_id:
            candidate_details = self.get_data(email_id=candidate_id)
        return Response(
            {
                'status': 200,
                'message': 'Details fetched successfully',
                'interviewer_details': interviewer_details,
                'candidate_details': candidate_details,
            },
            status=status.HTTP_200_OK
        )

    def get_data(self, email_id):
        """
        get the user data based on email id
        :param email_id: user mail id
        :return: return user data
        """
        if models.User.objects.filter(email=email_id).exists():
            user_obj = models.User.objects.get(email=email_id)
            return serializers.UserScheduleSerializer(user_obj).data

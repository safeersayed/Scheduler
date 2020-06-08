from rest_framework.views import APIView

from .services import SchedulerService

from rest_framework import status
from rest_framework.response import Response

scheduler_management_service = SchedulerService()


class ScheduleList(APIView):

    def get(self, request):
        try:
            return scheduler_management_service.schedule_list(interviewer_id=request.GET.get('interviewer_id'),
                                                              candidate_id=request.GET.get('candidate_id'))
        except Exception as e:
            print({e.__str__()})
            return Response(
                {
                    'status': 403,
                    'error': e.__str__()
                },
                status=status.HTTP_403_FORBIDDEN
            )

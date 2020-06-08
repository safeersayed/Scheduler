# views for user app
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from user.services import UserManagementServices

user_management_service = UserManagementServices()


class RegisterUser(APIView):

    def post(self, request):
        try:
            return user_management_service.register_user(data=request.data)
        except Exception as e:
            print({e.__str__()})
            return Response(
                {
                    'status': 403,
                    'error': e.__str__()
                },
                status=status.HTTP_403_FORBIDDEN
            )

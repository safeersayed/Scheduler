# url file for scheduler_api
from django.urls import path

from . import views

urlpatterns = [
    # get the list of schedule
    path('schedule-list/', views.ScheduleList.as_view(), name='schedule_list'),
]

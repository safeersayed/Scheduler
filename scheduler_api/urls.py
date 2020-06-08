
from django.urls import path

from . import views

urlpatterns = [
    path('schedule-list/', views.ScheduleList.as_view(), name='schedule_list'),
]

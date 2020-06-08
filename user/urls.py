# path defined for user app
from django.urls import path

from . import views

urlpatterns = [
    # to register the user
    path('add-user/', views.RegisterUser.as_view(), name='add_user'),
]

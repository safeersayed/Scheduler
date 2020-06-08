# managers for models
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


# base manager
class BaseManager(models.Manager):
    pass


# manager class for User
class UserManager(BaseManager, BaseUserManager):
    pass


# manager class for Scheduler
class SchedulerManager(BaseManager):
    pass

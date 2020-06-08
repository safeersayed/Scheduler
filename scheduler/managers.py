from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class BaseManager(models.Manager):
    pass


class UserManager(BaseManager, BaseUserManager):
    pass

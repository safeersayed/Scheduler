# Create your models here.

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from scheduler.managers import UserManager

USER_CATEGORY = (
    ('INTERVIEWER', 'Interviewer'),
    ('CANDIDATE', 'Candidate'),
)


class User(AbstractBaseUser):
    email = models.EmailField(_('Email address'), blank=True, null=True,
                              unique=True)
    user_category = models.CharField(_('User Category'), max_length=60, default='CANDIDATE', choices=USER_CATEGORY)
    available_date = models.DateField(_('available_from'), default=datetime.date.today)
    available_time_from = models.CharField(_('available time from'), max_length=5)
    available_time_to = models.CharField(_('available time to'), max_length=5)

    is_superuser = models.BooleanField(
        _('Admin status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    objects = UserManager()

    class Meta:
        db_table = 'USER'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.email}"

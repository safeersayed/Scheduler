from django.db import models
from user.models import User
from django.utils.translation import ugettext_lazy as _


class Scheduler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.CharField(_('Time_slot'), max_length=30)

    def __str__(self):
        return f"{self.user}"



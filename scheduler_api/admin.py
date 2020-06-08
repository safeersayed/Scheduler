from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Scheduler)
class SchedulerAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_slot')
    list_display_links = ('user', 'time_slot',)

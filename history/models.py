# coding=utf-8
# Python imports
# Django imports
from django.contrib.auth.models import User
from django.db import models
# Third party app imports
# Local app imports


class Activity(models.Model):
    activity = models.CharField(primary_key=True, null=False, blank=False, max_length=20)
    icon = models.CharField(null=False, blank=False, max_length=20)

    def __str__(self):
        return self.activity


class LogUser(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def pre_save(self):
        try:
            latest_log = LogUser.objects.filter(user=self.user).latest('timestamp')
            if latest_log.activity != self.activity or \
                    (latest_log.activity == self.activity and latest_log.description != self.description):
                self.save()
        except LogUser.DoesNotExist:
            self.save()
    
    def __str__(self):
        return self.user.username + ": " + self.activity.activity + " - " + self.description

import datetime

from django.db import models  # noqa F401
from django.utils import timezone
from django.contrib import admin


class Person(models.Model):  # noqa DJ10, DJ11
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.first_name

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class PersonNumber(models.Model):  # noqa: DJ10,DJ11,DJ08
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class LogModel(models.Model):  # noqa: DJ10,DJ11
    request = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    query = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request

    @admin.display(
        boolean=True,
        ordering="date_time",
        description="Published recently?",
    )
    def was_published_recently_log(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_time <= now

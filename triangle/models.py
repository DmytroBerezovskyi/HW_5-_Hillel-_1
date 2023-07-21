import datetime

from django.db import models  # noqa F401
from django.utils import timezone


class Person(models.Model):  # noqa DJ10, DJ11
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.first_name, self.last_name, self.email

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class PersonNumber(models.Model):  # noqa: DJ10,DJ11,DJ08
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

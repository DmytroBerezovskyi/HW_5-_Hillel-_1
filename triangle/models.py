from django.db import models  # noqa F401


class Person_model(models.Model):  # noqa DJ10, DJ11
    first_name_1 = models.CharField(max_length=200)
    last_name_1 = models.CharField(max_length=200)
    email_1 = models.EmailField(max_length=200)
# Create your models here.

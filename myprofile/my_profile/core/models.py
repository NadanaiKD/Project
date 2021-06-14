from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=300, default='')


class Email(models.Model):
    email = models.CharField(max_length=300, default='')

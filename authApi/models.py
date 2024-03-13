from django.db import models
from django.db import models


class authi(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=16)
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    roles = (('r', 'renter'), ('o','owner'))
    role = models.CharField(choices=roles, max_length=1)

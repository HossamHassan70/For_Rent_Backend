from django.db import models

from property_api.models import Property


class Role(models.TextChoices):
    RENTER = "Renter", "Renter"
    OWNER = "Owner", "Owner"
    ADMIN = "Admin", "Admin"


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=16, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=7, choices=Role.choices, default=Role.RENTER)
    validation_states = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    properties = models.ManyToManyField(
        Property, related_name="rented_by", through="UserPropertyRole"
    )


class UserPropertyRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=Role.choices, default=Role.RENTER)

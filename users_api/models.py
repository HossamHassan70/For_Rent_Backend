from django.db import models


class Role(models.TextChoices):
    RENTER = "Renter", "Renter"
    OWNER = "Owner", "Owner"
    ADMIN = "Admin", "Admin"


class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=7, choices=Role.choices, default=Role.RENTER)
    validation_states = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
   
    def str(self):
        return self.name

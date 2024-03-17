from django.db import models


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "user/%i.%s" % (instance.id, extension)

class Role(models.TextChoices):
    RENTER = "Renter", "Renter"
    OWNER = "Owner", "Owner"
    ADMIN = "Admin", "Admin"


class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16, blank=True)
    confirm_password =  models.CharField(max_length=16, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=7, choices=Role.choices, default=Role.RENTER)
    validation_states = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    profile_picture =  models.ImageField(upload_to=image_upload, default='blank_profile.png')

    def __str__(self):
        return self.name

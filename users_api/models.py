from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
from for_rent import settings

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return f"user/{instance.id}.{extension}"


class Role(models.TextChoices):
    RENTER = "Renter", "Renter"
    OWNER = "Owner", "Owner"
    ADMIN = "Admin", "Admin"


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=7, choices=Role.choices, default=Role.RENTER)
    validation_states = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(
        upload_to=image_upload,
        default= "user/blank_profile.png",
        validators=[
            FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"]),
        ],
        blank=True,
        null=True,
    )
    phone_number = PhoneNumberField(region="EG", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return (
                self.profile_picture.url
                if self.profile_picture
                else settings.DEFAULT_PROFILE_IMAGE
            )

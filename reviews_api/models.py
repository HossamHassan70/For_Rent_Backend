from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from property_api.models import Property
from users_api.models import User


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

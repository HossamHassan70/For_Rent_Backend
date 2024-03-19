from django.db import models
from users_api.models import User


class Request(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rejection_reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

from django.db import models
from property_api.models import Property
from users_api.models import User


class Request(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_request")
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='renter_request')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='requested_property')
    rejection_reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

from django.db import models

from users_api.models import User



class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('villa', 'Villa'),
    ]
    
    type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default='house')
    title = models.CharField(max_length=50)
    description = models.TextField()
    address = models.TextField()
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/property_images/', default='static/images/default_prop.jpg')
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_properties', null=True, blank=True)
    def str(self):
        return self.title
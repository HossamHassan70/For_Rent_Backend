from django.db import models
#from django.contrib.auth.models import User

class Property(models.Model):
   #Owner = models.ForeignKey(User, related_name='owned_properties', on_delete=models.CASCADE)
   #Renters = models.ManyToManyField(User, related_name='rented_properties')
    
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('villa', 'Villa'),
        # Add more choices as needed
    ]

    type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default='house' ) 
    title = models.CharField(max_length=200)
    address = models.TextField()
    description = models.TextField()
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='property_images/')
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()


    def __str__(self):
     return self.Title
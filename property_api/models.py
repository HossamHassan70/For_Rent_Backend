from django.db import models
#from django.contrib.auth.models import User

class Property(models.Model):
   #Owner = models.ForeignKey(User, related_name='owned_properties', on_delete=models.CASCADE)
   #Renters = models.ManyToManyField(User, related_name='rented_properties')
    ST_No = models.CharField(max_length=10)
    Building_No = models.CharField(max_length=10)
    Type = models.CharField(max_length=50)
    Address = models.TextField()
    Availability = models.BooleanField(default=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.ImageField(upload_to='property_images/')
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Rooms = models.IntegerField()
    Bathrooms = models.IntegerField()


    def __str__(self):
     return self.Title
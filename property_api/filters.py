import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = {
            'Type': ['exact'],
            'Price': ['exact', 'gte', 'lte'],
            'Address': ['icontains'],
            'Rooms': ['exact', 'gte', 'lte'],
            'Bathrooms': ['exact', 'gte', 'lte']
        }
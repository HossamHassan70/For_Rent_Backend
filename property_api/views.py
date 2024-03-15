from property_api.serializers import PropertySerializer
from property_api.models import Property

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PropertyClassViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def get_queryset(self):
        queryset = Property.objects.all()

        # Filter by type
        type_param = self.request.query_params.get('type', None)
        if type_param:
            queryset = queryset.filter(Type=type_param)

        # Filter by price
        price_param = self.request.query_params.get('price', None)
        if price_param:
            queryset = queryset.filter(Price=price_param)

        # Filter by rooms
        rooms_param = self.request.query_params.get('rooms', None)
        if rooms_param:
            queryset = queryset.filter(Rooms=rooms_param)
        
        # Filter by bathrooms
        bathrooms_param = self.request.query_params.get('bathrooms', None)
        if bathrooms_param:
            queryset = queryset.filter(Bathrooms=bathrooms_param)

        # Filter by address
        address_param = self.request.query_params.get('address', None)
        if address_param:
            queryset = queryset.filter(Address__icontains=address_param)

        return queryset

from property_api.serializers import PropertySerializer
from property_api.models import Property

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PropertyClassViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def get_queryset(self):
        queryset = Property.objects.all()

        type_param = self.request.query_params.get('type', None)
        if type_param:
            queryset = queryset.filter(Type=type_param)

        price_param = self.request.query_params.get('price', None)
        if price_param:
            queryset = queryset.filter(Price=price_param)

        rooms_param = self.request.query_params.get('rooms', None)
        if rooms_param:
            queryset = queryset.filter(Rooms=rooms_param)

        bathrooms_param = self.request.query_params.get('bathrooms', None)
        if bathrooms_param:
            queryset = queryset.filter(Bathrooms=bathrooms_param)

        address_param = self.request.query_params.get('address', None)
        if address_param:
            queryset = queryset.filter(Address__icontains=address_param)

        return queryset

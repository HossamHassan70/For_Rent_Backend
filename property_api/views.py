from property_api.serializers import PropertyCreateUpdateSerializer, PropertySerializer
from property_api.models import Property
from rest_framework import viewsets
from rest_framework.response import Response


class PropertyClassViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return PropertyCreateUpdateSerializer
        return PropertySerializer
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

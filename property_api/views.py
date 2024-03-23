from property_api.serializers import PropertySerializer
from property_api.models import Property
from rest_framework import viewsets, filters


class PropertyClassViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = Property.objects.all()

        title_param = self.request.query_params.get("title", None)
        if title_param:
            queryset = queryset.filter(title__icontains=title_param)

        type_param = self.request.query_params.get("type", None)
        if type_param:
            queryset = queryset.filter(type=type_param)

        rooms_param = self.request.query_params.get("rooms", None)
        if rooms_param:
            queryset = queryset.filter(rooms=rooms_param)

        bathrooms_param = self.request.query_params.get("bathrooms", None)
        if bathrooms_param:
            queryset = queryset.filter(bathrooms=bathrooms_param)

        return queryset

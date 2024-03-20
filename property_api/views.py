from property_api.serializers import PropertySerializer
from property_api.models import Property
from rest_framework import viewsets, filters
from django.db .models import Q

class PropertyClassViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    filter_backends = [filters.SearchFilter]  # Only SearchFilter for now

    search_fields = ['title', 'description', 'address']  # Fields for full-text search

    def get_queryset(self):
        queryset = Property.objects.all()
        query = self.request.query_params.get("q")

        # Apply SearchFilter
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query) | Q(address__icontains=query)
            )

        # Add your additional filtering logic here
        price_gt = self.request.query_params.get('price_gt', None)
        if price_gt:
            try:
                price_gt = int(price_gt)
                queryset = queryset.filter(price__gte=price_gt)
            except ValueError:
                pass  # Handle invalid price format

        rooms_exact = self.request.query_params.get('rooms', None)
        if rooms_exact:
            try:
                rooms_exact = int(rooms_exact)
                queryset = queryset.filter(rooms=rooms_exact)
            except ValueError:
                pass  # Handle invalid room count format

        bathrooms_exact = self.request.query_backends.get('bathrooms', None)
        if bathrooms_exact:
            try:
                bathrooms_exact = int(bathrooms_exact)
                queryset = queryset.filter(bathrooms=bathrooms_exact)
            except ValueError:
                pass  # Handle invalid bathroom count format

        type_exact = self.request.query_params.get('type', None)
        if type_exact:
            queryset = queryset.filter(type__exact=type_exact)

        return queryset

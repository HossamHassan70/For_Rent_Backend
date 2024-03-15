from rest_framework import viewsets
from reviews_api.models import Review
from reviews_api.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

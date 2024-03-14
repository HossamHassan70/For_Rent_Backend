from django.http import Http404
from reviews_api.models import Review
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reviews_api.serializers import ReviewSerializer


class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    def get_review(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404("Review does not exist")

    def get(self, request, pk):
        review = self.get_review(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk):
        review = self.get_review(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_review(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
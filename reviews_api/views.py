from django.http import Http404
from reviews_api.models import Review
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reviews_api.serializers import ReviewSerializer


# from django.shortcuts import get_object_or_404, redirect, render
# from reviews_api.forms import ReviewForm

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
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# using front html

# def review_list(request):
#     reviews = Review.objects.all()
#     return render(request, "reviews/review_list.html", {"reviews": reviews})


# def review_detail(request, pk):
#     review = Review.objects.get(pk=pk)
#     return render(request, "reviews/review_detail.html", {"review": review})


# def create_review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("review_list")
#     else:
#         form = ReviewForm()
#         return render(request, "reviews/create_review.html", {"form": form})


# def update_review(request, pk):
#     review = Review.objects.get(pk=pk)
#     if request.method == "POST":
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             form.save()
#             return redirect("review_list")
#     else:
#         form = ReviewForm(instance=review)
#         return render(request, "reviews/update_review.html", {"form": form, "review": review})

# def review_delete(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.method == "POST":
#         review.delete()
#         return redirect("review_list")
#     return render(request, "reviews/review_delete_confirm.html", {"review": review})
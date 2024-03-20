from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Define your other view methods (create, update, destroy, etc.) here

    def partial_update(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(
                "Serializer errors:", serializer.errors
            )  # Add this line to print serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

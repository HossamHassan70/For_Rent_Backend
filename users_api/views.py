from django.forms import ValidationError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Uncomment for authentication

    def get_queryset(self):
        """
        Filter queryset based on user role (admins see all, others see themselves).
        """
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=user.pk)

    def perform_create(self, serializer):
        """
        Override to create a user with the provided role.
        """
        serializer.save(role=self.request.data.get("role"))

    def create(self, request, *args, **kwargs):
        """
        Custom logic for POST request (creating a user).
        Raises an exception for invalid data and returns a 201 Created response on success.
        """
        serializer = self.get_serializer(data=request.data)
        try:
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        except ValidationError as e:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Custom logic for PUT request (updating a user).
        Allows full replacement of user data (consider using PATCH for partial updates).
        Performs authorization checks and raises an exception for invalid data.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        if not request.user.is_staff and instance.pk != request.user.pk:
            return Response(
                {"detail": "You are not authorized to update this user."},
                status=HTTP_403_FORBIDDEN,
            )

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Custom logic for PATCH request (partially updating a user).
        """
        return self.update(request, pk, partial=True, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Custom logic for DELETE request (deleting a user).
        Requires admin privileges for deletion.
        Performs authorization checks.
        """
        instance = self.get_object()

        if not request.user.is_staff:
            return Response(
                {"detail": "You are not authorized to delete users."},
                status=HTTP_403_FORBIDDEN,
            )

        instance.delete()
        return Response(
            {"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )

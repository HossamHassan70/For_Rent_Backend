from rest_framework import routers
from .views import UserViewSet
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls

"""
List users: /api/users/
Create a user: /api/users/ (POST request)
Retrieve a user: /api/users/{user_id}/
Update a user: /api/users/{user_id}/ (PUT or PATCH request)
Delete a user: /api/users/{user_id}/ (DELETE request)
"""

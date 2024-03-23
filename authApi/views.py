import jwt
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from for_rent import settings
from users_api.models import User
from users_api.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserEmailVerification


# Create your views here.
class authiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(
                {"error": "Please provide both username and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        if user.password != password:
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = UserSerializer(user)

        # pay load hna
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phoneNumber": str(user.phone_number),
            "profilePicture": user.get_profile_picture_url(),
            "role": user.role,
            "registration_date": str(user.registration_date),
            "validation_states": user.validation_states,
        }

        # JWT
        refresh = RefreshToken.for_user(user)
        # refresh.set_exp(lifetime=timedelta(hours=1))

        # refresh tk
        refresh["user"] = user_data

        return Response(
            {
                # 'user': serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


class VerifyCode(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        # Extract JWT token from Authorization header
        token = request.headers.get("Authorization").split(" ")[1]
        # verify and decode token
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        print(f"this is decoded Token {decoded_token}")

        # get email decoded
        email = decoded_token.get("user").get(
            "email"
        )  # Extract email from decoded token
        print(f"this is user email {email}")

        # 3 search for UserEmailVerification with matching email
        try:
            user_verification = UserEmailVerification.objects.get(email=email)
            user = User.objects.get(email=email)
        except UserEmailVerification.DoesNotExist:
            return Response(
                {"error": "No verification record found for this email"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Compare code in request with code in UserEmailVerification instance
        if str(user_verification.code) == str(request.data.get("code")):
            # if matching, change states to true
            user.validation_states = True
            user.save()
            return Response(
                {"message": "Email verification successful"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid verification code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

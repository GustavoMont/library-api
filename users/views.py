from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from permissions.users import UsersPermissions
from rest_framework import permissions
from users import models, serializers
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here
# 
class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = serializers.UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [UsersPermissions]

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.LibraryTokenSerializer
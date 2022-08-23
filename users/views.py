from rest_framework import viewsets
from users import models, serializers
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.LibraryTokenSerializer
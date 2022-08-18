from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from users import models, serializers

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = [DjangoModelPermissions]
from rest_framework import routers
from users.views import UserViewset

router = routers.DefaultRouter()

router.register(r'users', UserViewset)

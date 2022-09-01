from rest_framework import routers
from book.views import BookViewset

router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='books')
from rest_framework import viewsets
from book.serializers import BookSerializer
from book.models import Book

# Create your views here.
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


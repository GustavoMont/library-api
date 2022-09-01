from urllib import request
from rest_framework import viewsets
from book.serializers import BookSerializer
from book.models import Book
from permissions.books import BookPermission

# Create your views here.
class BookViewset(viewsets.ModelViewSet):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [BookPermission]

    def get_queryset(self):
        if self.request.user.id:
            user_group = list(self.request.user.groups.values())[0]
            if 'ADMIN' in user_group['name']:
                return Book.objects.all() 
        print(Book.objects.filter(available = True))
        return Book.objects.filter(quantity__gt = 0, available = True)


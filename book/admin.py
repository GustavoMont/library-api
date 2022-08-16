from django.contrib import admin
from book.models import Book

# Register your models here.
class Books(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Book, Books)
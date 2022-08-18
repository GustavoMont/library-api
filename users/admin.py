from django.contrib import admin

from .models import User

# Register your models here.
class Users(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'can_borrow']
    list_display_links = ['id', 'full_name']
    search_fields = ('first_name',)

admin.site.register(User, Users)
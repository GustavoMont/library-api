from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.
class Users(UserAdmin):
    list_display = ['id', 'full_name', 'email', 'can_borrow']
    list_display_links = ['id', 'full_name']
    search_fields = ('first_name',)
    fieldsets = (
        (
            'Fields',
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "cpf",
                    'is_active',
                    'can_borrow',
                    'password'
                )
            },
        ),
        ("Permissions", {"fields": ( "groups", "user_permissions","is_staff",)}),
        (
            "Personal",
            {
                "fields": (
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username','cpf','password1', 'password2', 'groups'),
        }),
    )


admin.site.register(User, Users)
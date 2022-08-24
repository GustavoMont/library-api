from rest_framework import permissions
from rest_framework.permissions import BasePermission
from permissions.LibraryBasePermission import LibraryBasePermission


class UsersPermissions(LibraryBasePermission):
    message = "Não pode accesar essa informação"
    alLowed_groups = ['ADMIN']
    safe_methods = ['POST', 'OPTIONS', 'HEAD']

    def has_permission(self, request, view):
        if request.META['PATH_INFO'] == '/users/':
            return self.get_user_group(request.user) in self.alLowed_groups
        else:
            return True

    def has_object_permission(self, request, view, obj):   
        if request.method in self.safe_methods:
            return True
        if self.get_user_group(request.user) in self.alLowed_groups:
            return True
        else:
            return obj.id == request.user.id
            
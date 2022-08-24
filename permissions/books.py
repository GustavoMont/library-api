from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions, status

from permissions.LibraryBasePermission import LibraryBasePermission




class BookPermission(LibraryBasePermission):
    message = "Ei ei ei, quem ta lendo é gaykkkkkkkkkk"
    alLowed_groups = ['ADMIN']

    def has_permission(self, request, view):
        user_group = self.get_user_groups(request.user)
        response = {
            "message": self.message,
            "status_code": status.HTTP_403_FORBIDDEN,
        }
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if user_group not in self.alLowed_groups:
                raise PermissionDenied(response)
                   

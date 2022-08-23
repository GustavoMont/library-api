from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions, status


alLowed_groups = ['ADMIN']

class BookPermission(permissions.BasePermission):
    message = "Ei ei ei, quem ta lendo é gaykkkkkkkkkk"

    def has_permission(self, request, view):
        user_group = list(request.user.groups.values())
        response = {
            "message": self.message,
            "status_code": status.HTTP_403_FORBIDDEN,
        }
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if user_group not in alLowed_groups:
                raise PermissionDenied(response)
                   

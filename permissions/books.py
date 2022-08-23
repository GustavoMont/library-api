from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions, status


class BookPermission(permissions.BasePermission):
    message = "Ei ei ei, quem ta lendo é gaykkkkkkkkkk"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            print(request.user)
            response = {
                "message": self.message,
                "status_code": status.HTTP_403_FORBIDDEN,
            }
            raise PermissionDenied(response)

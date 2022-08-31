from email import message
from .LibraryBasePermission import LibraryBasePermission

class LoansPermissions(LibraryBasePermission):
    alLowed_groups = ['ADMIN']

    def has_object_permission(self, request, view, obj):
        forbidden_fileds = ['returned_at', 'returned', 'return_date']
        if self.get_user_group(request.user) in self.alLowed_groups:
            return True
        for field in request.data.keys():
            if field in forbidden_fileds:
                return False
        return obj.user.id == request.user.id

    def has_permission(self, request, view):
        if request.META['PATH_INFO'] == '/loans/':
            return self.get_user_group(request.user) in self.alLowed_groups
        return True
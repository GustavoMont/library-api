from rest_framework.permissions import BasePermission

class LibraryBasePermission(BasePermission):
    alLowed_groups = ['ADMIN']   
    safe_methods = ['GET']


    def get_user_group(self, user):
        user_groups = list(user.groups.values())
        if len(user_groups) == 0:
            return  'NOT_AUTHENTICATED'
        return list(user.groups.values())[0]['name']

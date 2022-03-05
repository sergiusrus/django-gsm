from rest_framework import permissions


class IsApiUser(permissions.BasePermission):
    """
    Allows access only to api_users group members.
    """
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='api_users'):
            return True
        return False

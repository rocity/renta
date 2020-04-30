from rest_framework import permissions


class CanManageProfile(permissions.BasePermission):
    """
    Profile Management Perms

    - Only owner and admin can update a profile
    - Only admins can delete profiles (This may change in the future)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method in ['DELETE']:
            return request.user.is_staff

        return obj == request.user or request.user.is_staff


class CanSignUp(permissions.BasePermission):
    """
    Signup View Perms

    - Only anon users can access the signup view
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False
        return True

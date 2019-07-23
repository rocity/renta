from rest_framework import permissions


class CanManageListing(permissions.BasePermission):
    """
    Listing Management Perms
    - Only the owner and admin can update/delete a listing
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user or request.user.is_staff

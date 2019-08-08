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


class CanManageListingImage(permissions.BasePermission):
    """
    ListingImage Management Perms
    - Only the Listing owner and admin can
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff

        return obj.listing.user == request.user or request.user.is_staff

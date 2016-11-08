from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsReadOnly(BasePermission):
    """
    The request is a read-only request.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsSuperuser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

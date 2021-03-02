from rest_framework import permissions

from .models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
        ) or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
        ) or request.user.is_superuser


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
        ) or request.user.role == User.MODERATOR


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )

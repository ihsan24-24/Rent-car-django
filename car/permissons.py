from rest_framework import permissions


class IsStaffOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # gelen request methodu safe method yani get isteği ise izin ver
        if request.method in permissions.SAFE_METHODS:
            return True
        # user var mı ve user staff mı?
        return bool(request.user and request.user.is_staff)
from rest_framework import permissions
from .models import Store


class HasPhone(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.query_params.get('phone'):
            return True
        return False


class IsEmployeeInStore(permissions.BasePermission):
    def has_permission(self, request, view):
        phone = request.query_params.get('phone')
        store_id = request.data.get('store')
        if Store.objects.filter(id=store_id, employee__phone=phone).exists():
            return True
        return False

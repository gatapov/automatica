from django.contrib import admin
from .models import Store, Employee, Visit


class StoreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class VisitAdmin(admin.ModelAdmin):
    search_fields = ('store__name', 'employee__name')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
       return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Store, StoreAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Visit, VisitAdmin)

from django.contrib import admin
from .models import Contact, Registration
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Contact)
class RegistrationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email', 'faculty', 'level')
    list_filter = ('faculty', 'department', 'level')
    search_fields = ('faculty', 'department', 'level', 'first_name', 'middle_name', 'last_name')

admin.site.register(Registration, RegistrationAdmin)
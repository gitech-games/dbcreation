from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from import_export import resources
from .models import Employee, FileUpload, CreateDB, TableData, UserModel, UserMaster, WorkSpace

admin.site.register(FileUpload)
admin.site.register(CreateDB)
admin.site.register(TableData)
admin.site.register(WorkSpace)
admin.site.register(UserModel)
admin.site.register(UserMaster)

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass



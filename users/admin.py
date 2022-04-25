from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'email',  ]

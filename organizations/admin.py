from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from organizations.models import Organization, MethodicalAssociation, MetodicalMember
from organizations.resources import OrganizationResource


@admin.register(Organization)
class OrganizationAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'region', 'district', 'locality', 'territoriAlaffiliation' ,'published', ]
    exclude = ('edit_date',)
    list_display_links = ('name',)
    resource_class = OrganizationResource


@admin.register(MethodicalAssociation)
class MethodicalAssociationAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'user', 'organization', 'name',]

@admin.register(MetodicalMember)
class MetodicalMemberAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'metodicalAssociation', 'name', ]
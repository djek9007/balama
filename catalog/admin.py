from django.contrib import admin
from django.contrib.admin import AdminSite
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from catalog.models import Region, District, Locality, TerritorialAffiliation, Language, Subject, ClassRoom
from catalog.resources import RegionResource, DistrictResource, LocalityResource


class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        #for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list


@admin.register(Region)
class RegionAdmin(ImportExportActionModelAdmin,ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("name",)
    save_on_top = True
    list_display = ['id', 'name', 'published', ]
    resource_class = RegionResource
    list_display_links = ("name",)

    exclude = ('edit_date',)
    # readonly_fields = ('published',)

    list_per_page = 20

@admin.register(District)
class DistrictAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DistrictResource
    search_fields = ("name",)
    save_on_top = True
    list_display = ['id', 'name', 'region', ]
    actions = ['unpublish', 'publish', ]
    list_display_links = ("name",)

    # readonly_fields = ('published',)
    exclude = ('edit_date',)

    list_filter = ('region',)

    list_per_page = 20


@admin.register(Locality)
class LocalityAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'region', 'district', 'published', ]
    resource_class = LocalityResource
    list_filter = ['region', 'district',]
    exclude = ('edit_date',)
    list_display_links = ('name',)
    search_fields = ("name",)
    save_on_top = True


@admin.register(TerritorialAffiliation)
class TerritorialAffiliationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published', ]
    exclude = ('edit_date',)
    search_fields = ("name",)
    save_on_top = True

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    exclude = ('edit_date',)
    search_fields = ("name",)
    save_on_top = True

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']
    list_filter = ('language',)
    search_fields = ("name",)
    save_on_top = True


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ("name",)
    save_on_top = True



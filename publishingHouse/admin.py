from django.contrib import admin

# Register your models here.
from publishingHouse.models import PublishingHouse, TextBook, YearPublising

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(YearPublising)
class YearPublisingAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TextBook)
class TextBookAdmin(admin.ModelAdmin):
    list_display = ('publishingHouse', 'subject', 'classroom', 'yearPublishing',)
    list_filter = ('publishingHouse', 'subject', 'classroom', 'yearPublishing',)

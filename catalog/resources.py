from django.forms import Field
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from catalog.models import Region, District, Locality


class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        exclude = ['published', 'created_date', 'edit_date',]


class DistrictResource(resources.ModelResource):
    # region = fields.Field(column_name='Наименование Области/города (ID)', attribute='region', widget=ForeignKeyWidget(Region, 'name'))
    # name = fields.Field(column_name='Наименование района', attribute='name',)
    # region_id = fields.Field(column_name='ID Область/город',)

    class Meta:
        model = District
        fields = ['id','region', 'name', ]

    def dehydrate_region_id(self, district):
        region_id = getattr(district.region, 'id', 'unkwoun')
        return '{}'.format(region_id,)


class LocalityResource(resources.ModelResource):
    # region = fields.Field(column_name='Наименование Области/города (ID) ', attribute='region', widget=ForeignKeyWidget(Region, 'name'))
    # district = fields.Field(column_name='Наименование Районa (ID) ', attribute='district', widget=ForeignKeyWidget(District, 'name'))
    # name = fields.Field(column_name='Наименование населенного пункта', attribute='name', )

    # region_id = fields.Field(column_name='ID Область/город',)
    # district_id = fields.Field(column_name='ID района',)

    class Meta:
        model = Locality
        fields = ('id','region', 'district', 'name',)

    def dehydrate_region_id(self, locality):
        region_id = getattr(locality.region, 'id', 'unkwoun')
        return '{}'.format(region_id,)


    def dehydrate_district_id(self, locality):
        district_id = getattr(locality.district, 'id', 'unkwoun')
        return '{}'.format(district_id,)
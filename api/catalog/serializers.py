from rest_framework import serializers
from catalog.models import Region, District, Locality, TerritorialAffiliation, Language, ClassRoom, Subject


class DistrictSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Района"""
    group_by_locality = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ['id', 'name', 'region', 'group_by_locality', ]

    def get_group_by_locality(self, instance):
        locality = Locality.objects.order_by('name').filter(district=instance)
        return LocalitySerializer(locality, many=True).data


class RegionSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Область/город"""
    group_by_districts = serializers.SerializerMethodField()


    class Meta:
        model = Region
        fields = ['id','name', 'group_by_districts',]

    def get_group_by_districts(self, instance):
        district = District.objects.order_by('name').filter(region=instance)
        return DistrictSerializer(district, many=True).data


class LocalitySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели населенного пункта"""

    class Meta:
        model = Locality
        fields = ('id',  'region', 'district', 'name',)


class TerritorialAffiliationSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели территориальной принадлежности"""

    class Meta:
        model = TerritorialAffiliation
        fields = ('id', 'name',)


class LanguageSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели язык"""

    class Meta:
        model = Language
        fields = ('id', 'name',)


class ClassRoomSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода всех классов"""

    class Meta:
        model = ClassRoom
        fields = ('id', 'name',)


class SubjectSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели предметов"""

    class Meta:
        model = Subject
        fields = ('id', 'name', 'language',)
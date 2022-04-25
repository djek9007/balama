from rest_framework import serializers

from organizations.models import Organization, MethodicalAssociation, MetodicalMember


class OrganizationSerializer(serializers.ModelSerializer):
    """Список организации"""
    # region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # locality = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # territoriAlaffiliation = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # language = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'region', 'district', 'locality', 'territoriAlaffiliation', 'language', 'name',)

class MethodicalAssociationSerializer(serializers.ModelSerializer):
    """Методическое объединение"""

    class Meta:
        model = MethodicalAssociation
        fields = ('id', 'user', 'organization', 'name',)


class MetodicalMemberSerializer(serializers.ModelSerializer):
    """Члены методического объединение"""

    class Meta:
        model = MetodicalMember
        fields =('id', 'metodicalAssociation', 'name',)
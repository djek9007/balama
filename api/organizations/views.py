from django.http import request
from rest_framework import viewsets


from api.organizations.serializers import OrganizationSerializer, MethodicalAssociationSerializer, \
    MetodicalMemberSerializer

from organizations.models import Organization, MethodicalAssociation, MetodicalMember


class OrganizationsViewSet(viewsets.ModelViewSet):
    """Модель Организации"""
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.filter(published=True)


class MethodicalAssociationViewSet(viewsets.ModelViewSet):
    """Модель методического объединение"""
    serializer_class = MethodicalAssociationSerializer
    queryset = MethodicalAssociation.objects.filter(published=True)


class MetodicalMemberViewSet(viewsets.ModelViewSet):
    """Модель методического объединение"""
    serializer_class = MetodicalMemberSerializer
    queryset = MetodicalMember.objects.filter(published=True)



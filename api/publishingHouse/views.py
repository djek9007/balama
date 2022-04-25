from rest_framework import permissions, viewsets

from publishingHouse.models import PublishingHouse, TextBook, YearPublising
from api.publishingHouse.serializers import PublishingHouseSerializer,  TextBookSerializer, YearPublisingSerializer


class PublishingHouseViewSet(viewsets.ModelViewSet):
    """Вывод всех издательств"""
    serializer_class = PublishingHouseSerializer
    queryset = PublishingHouse.objects.filter(published=True)


class TextBookViewSet(viewsets.ModelViewSet):
    """Вывод всех учебников"""
    serializer_class = TextBookSerializer
    queryset = TextBook.objects.filter(published=True)


class YearPublishingViewSet(viewsets.ModelViewSet):
    """Вывод всех годов издании"""
    serializer_class = YearPublisingSerializer
    queryset = YearPublising.objects.filter(published=True)


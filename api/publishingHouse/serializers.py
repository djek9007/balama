from rest_framework import serializers

from publishingHouse.models import PublishingHouse, TextBook, YearPublising


class PublishingHouseSerializer(serializers.ModelSerializer):
    """Серилайзер для модели Издательство"""

    class Meta:
        model = PublishingHouse
        fields = ('id', 'name',)



class TextBookSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели учебников"""
    # publishingHouse = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # subject = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # classroom = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # yearPublishing = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # language = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = TextBook
        fields = ('id',
                  'publishingHouse',
                  'subject',
                  'classroom',
                  'yearPublishing',
                  'language',
                  'description',
                  'cover',
                  'link',
                  'file',)


class YearPublisingSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода всех издании по годам издательство"""
    class Meta:
        model = YearPublising
        fields = ('id', 'name',)


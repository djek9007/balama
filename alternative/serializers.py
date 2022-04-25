from rest_framework import serializers

from .models import Alternative


class AlternativeSerializer(serializers.ModelSerializer):
    """Вывод всех выбранных учебников"""
    # publishingHouse = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # subject = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # classroom = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # yearPublishing = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Alternative
        fields = "__all__"

from rest_framework import serializers
from .models import ArtType, Exhibit, Gallery, Position


class ArtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtType
        fields = "__all__"


class ExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class ExhibitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = "__all__"


class GalleryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class PositionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"

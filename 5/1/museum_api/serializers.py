from rest_framework import serializers
from .models import ArtType, Exhibit, Gallery, Position, Tour, User, Article
from datetime import date


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

    def validate_area(self, area: float):
        if area <= 0:
            raise serializers.ValidationError("Area can't be negative")
        return area

    def validate_floor(self, floor: int):
        if floor <= 0:
            raise serializers.ValidationError("Floor can't be negative")
        return floor

    def validate_number(self, number: int):
        if number <= 0:
            raise serializers.ValidationError("Number can't be negative")
        return number


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)

    def validate_birth_date(self, birth_date: date):
        if birth_date >= date.today():
            raise serializers.ValidationError("Birthday can't be in the future.")
        return birth_date


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

from rest_framework import viewsets, permissions
from .models import ArtType, Exhibit, Gallery, Position, Tour, User, Article, Review
from .serializers import (
    ArtTypeSerializer,
    ExhibitSerializer,
    GallerySerializer,
    PositionSerializer,
    TourSerializer,
    UserSerializer,
    ArticleSerializer,
    ReviewSerializer,
)


class ArtTypeViewSet(viewsets.ModelViewSet):
    queryset = ArtType.objects.all()
    serializer_class = ArtTypeSerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ExhibitViewSet(viewsets.ModelViewSet):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ExhibitSerializer
        return self.serializer_class


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return GallerySerializer
        return self.serializer_class


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PositionSerializer
        return self.serializer_class


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TourSerializer
        return self.serializer_class


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_by_action = {
        "list": [permissions.IsAuthenticated],
        "create": [permissions.IsAdminUser],
        "retrieve": [permissions.IsAuthenticated],
        "update": [permissions.IsAdminUser],
        "partial_update": [permissions.IsAdminUser],
        "destroy": [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserSerializer
        return self.serializer_class


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PositionSerializer
        return self.serializer_class


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PositionSerializer
        return self.serializer_class


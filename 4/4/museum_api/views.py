from rest_framework import viewsets, permissions
from .models import ArtType, Exhibit, Gallery, Position, Tour
from .serializers import (
    ArtTypeSerializer,
    ExhibitSerializer,
    GallerySerializer,
    PositionSerializer,
    TourSerializer,
    ExhibitDetailSerializer,
    GalleryDetailSerializer,
    PositionDetailSerializer,
)


class ArtTypeViewSet(viewsets.ModelViewSet):
    queryset = ArtType.objects.all()
    serializer_class = ArtTypeSerializer
    permission_classes_by_action = {"create": [permissions.IsAuthenticated]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ExhibitViewSet(viewsets.ModelViewSet):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    permission_classes_by_action = {"create": [permissions.IsAuthenticated]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ExhibitDetailSerializer
        return self.serializer_class


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes_by_action = {"create": [permissions.IsAuthenticated]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return GalleryDetailSerializer
        return self.serializer_class


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes_by_action = {"create": [permissions.IsAuthenticated]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PositionDetailSerializer
        return self.serializer_class


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes_by_action = {"create": [permissions.IsAuthenticated]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TourSerializer
        return self.serializer_class

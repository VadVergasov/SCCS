"""
URL configuration for lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from museum_api.views import ArtTypeViewSet, ExhibitViewSet, GalleryViewSet, PositionViewSet, TourViewSet, UserViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

router = routers.DefaultRouter()
router.register(r"arttypes", ArtTypeViewSet)
router.register(r"exhibits", ExhibitViewSet)
router.register(r"galleries", GalleryViewSet)
router.register(r"positions", PositionViewSet)
router.register(r"tours", TourViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", views.index, name="index"),
    path("articles/<int:id>/", views.get_article, name="article_detail"),
    path("privacy/", views.privacy, name="privacy"),
    path("about/", views.about, name="about"),
    path("articles/", views.articles, name="articles"),
    path("contacts/", views.contacts, name="contacts"),
    path("promos/", views.promos, name="promos"),
    path("submit-review/", views.submit_review, name="submit-review"),
]

from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", views.UserViewSet, basename="user")
router.register(r"category", views.CategoryViewSet, basename="category")
router.register(r"airticle", views.AirticalViewSet, basename="airticle")

urlpatterns = [
    path("", views.index, name="index"),
    path("", include(router.urls)),  # Include the router's URLs

]


from django.urls import path, include
from api_search import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", views.UserViewSet, basename="user")
router.register(r"category", views.CategoryViewSet, basename="category")
router.register(r"article", views.ArticalViewSet, basename="article")

urlpatterns = [
    path("", include(router.urls)),  # Include the router's URLs

]


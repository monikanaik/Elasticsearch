from django.urls import path, include
from api_search import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", views.UserViewSet, basename="user")
router.register(r"category", views.CategoryViewSet, basename="category")
router.register(r"article", views.ArticalViewSet, basename="article")

urlpatterns = [
    path("art/",views.search_article),
    path("user/<str:query>/", views.SearchUsers.as_view()),
    path("category/<str:query>/", views.SearchCategories.as_view()),
    path("article/<str:query>/", views.SearchArticles.as_view()),
    path("", include(router.urls)),  # Include the router's URLs

]


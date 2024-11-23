from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Article
from django.contrib.auth.models import User
from .serializers import UserSerializer, CategorySerializer, ArticleSerializer
# Create your views here.




class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset= User.objects.all()
    

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class ArticalViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
from django.shortcuts import render
from elasticsearch_dsl.query import MultiMatch
from app.documents import BookDocument
from rest_framework.viewsets import ModelViewSet
from app.models import Category, Article
from django.contrib.auth.models import User
from app.serializers import UserSerializer, CategorySerializer, ArticleSerializer


def index(request):
    q = request.GET.get("q")
    context = {}
    if q:
        query = MultiMatch(query=q, fields=["title", "description"],fuzziness="AUTO")
        response = BookDocument.search().query(query).execute()
        s = BookDocument.search().query("match", title=q)[0:5]
        print(s.to_queryset())
        context["books"] = response
    return render(request, "app/index.html", context)




class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset= User.objects.all()
    

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class AirticalViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    

    
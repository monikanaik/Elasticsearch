from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Article
from django.contrib.auth.models import User
from .serializers import UserSerializer, CategorySerializer, ArticleSerializer
from api_search.documents import ArticleDocument, UserDocument, CategoryDocument
from django.http import HttpResponse
from elasticsearch_dsl import Q
import abc
from django.http import HttpResponse
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

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

def search_article(request):
    # Looks up all the articles that contain `How to` in the title.
    """
    Looks up all the articles that:
    1) Contain 'language' in the 'title'
    2) Don't contain 'ruby' or 'javascript' in the 'title'
    3) And contain the query either in the 'title' or 'description'
    """
    query = "How to"
    q = Q(
        "multi_match",
        query=query,
        fields=[
            "title"
        ])
    search = ArticleDocument.search().query(q)
    response = search.execute()

    # print all the hits
    for hit in search:
        print(hit.title)

    query = "djengo"  # notice the typo
    q = Q(
        "multi_match",
        query=query,
        fields=[
            "title"
        ],
        fuzziness="auto")
    search = ArticleDocument.search().query(q)
    response = search.execute()

    # print all the hits
    for hit in search:
        print(hit.title)
    return HttpResponse(hit.title)









class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f"Found {response.hits.total.value} hit(s) for query: '{query}'")

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


# views


class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q("bool",
                 should=[
                     Q("match", username=query),
                     Q("match", first_name=query),
                     Q("match", last_name=query),
                 ], minimum_should_match=1)


class SearchCategories(PaginatedElasticSearchAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument

    def generate_q_expression(self, query):
        return Q(
                "multi_match", query=query,
                fields=[
                    "name",
                    "description",
                ], fuzziness="auto")


class SearchArticles(PaginatedElasticSearchAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q(
                "multi_match", query=query,
                fields=[
                    "title",
                    "author",
                    "type",
                    "content"
                ], fuzziness="auto")


        
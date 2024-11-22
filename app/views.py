from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch_dsl.query import MultiMatch, MoreLikeThis
from app.documents import BookDocument
from elasticsearch_dsl import Search

def index(request):
    q = request.GET.get("q")
    context = {}
    if q:
        query = MultiMatch(query=q, fields=["title", "description"],fuzziness="AUTO")
        response = BookDocument.search().query(query).execute()
        # s = BookDocument.search().query("match", title=q)
        context["books"] = response
    return render(request, "app/index.html", context)





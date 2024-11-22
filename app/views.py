from django.shortcuts import render
from elasticsearch_dsl.query import MultiMatch
from app.documents import BookDocument
import logging

logger = logging.getLogger(__name__)


def index(request):
    q = request.GET.get("q")
    context = {}
    if q:
        try:
            logger.info(f"Received search query: {q}")
            query = MultiMatch(query=q, fields=["title", "description"], fuzziness="AUTO")
            response = BookDocument.search().query(query).execute()
            s = BookDocument.search().query("match", title=q)[0:5]
            logger.info(f"result in queryset {s}")
            logger.info(f"Search query executed successfully. Found {len(response)} results.")
            context["books"] = response
        except Exception as e:
            logger.error(f"An error occurred: {e}")
    return render(request, "app/index.html", context)

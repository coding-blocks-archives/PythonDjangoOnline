from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import (
  ListAPIView, 
  RetrieveAPIView,
  UpdateAPIView,
  RetrieveUpdateAPIView,
  ListCreateAPIView
)

from api import serializers, models

# Create your views here.
class ArticlesListView(ListCreateAPIView):
  serializer_class = serializers.ArticleSerializer

  def get_queryset(self):
    query = {}
    for key, value in self.request.GET.items():
      query["{}__icontains".format(key)] = value

    return models.Article.objects.filter(**query)

class ArticlesDetailView(RetrieveUpdateAPIView):
  queryset = models.Article.objects.all()
  serializer_class = serializers.ArticleSerializer 

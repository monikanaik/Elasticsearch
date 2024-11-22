from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Article, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"


    def create(self, validated_data):
        author_data = validated_data.pop('author')
        categories_data = validated_data.pop('categories')

        author = User.objects.create(**author_data)
        categories = Category.objects.filter(name__in=[category_data['name'] for category_data in categories_data])
        
        article = Article.objects.create(author=author, **validated_data)
        article.categories.set(categories)
        return article
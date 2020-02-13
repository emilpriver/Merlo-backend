from rest_framework import serializers
from merlo.posts.models import Article, Category


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    thumbnail = serializers.ImageField()

    class Meta:
        models: Category


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField(required=False)
    content = serializers.CharField()
    thumbnail = serializers.ImageField()
    category = CategorySerializer(many=False)

    class Meta:
        models: Article

    def create(self, validated_data):
        return Article(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.slug = validated_data.get('slug', instance.created)
    #     return instance

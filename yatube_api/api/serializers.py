from rest_framework import serializers

from posts.models import Post, Comment, Group


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')


class PostSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author',
                  'image', 'group', 'comments')

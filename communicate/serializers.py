from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = Comment
        fields = ['Commentid', 'commnetInfo', 'user_id', 'created_at', 'comment']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("Commentid", "commnetInfo", "comment", "user_id")

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['Commentid', 'commnetInfo', 'user_id', 'created_at', 'comment', 'likes', 'dislike']


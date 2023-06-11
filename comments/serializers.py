from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='user.profile.profile_pic.url'
    )
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'created_on', 'updated_on', 'event',
            'content', 'is_owner', 'profile_id', 'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for Comment Detail View

    """
    event = serializers.ReadOnlyField(source='event.id')

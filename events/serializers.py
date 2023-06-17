# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Event
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Events model
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='user.profile.profile_pic.url'
    )
    comments_count = serializers.ReadOnlyField()
    interested_count = serializers.ReadOnlyField()
    join_request = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    class Meta:
        model = Event
        fields = [
            'id', 'user', 'is_owner', 'created_on', 'updated_on', 'title',
            'category', 'sub_category', 'event_start_date', 'event_end_date',
            'content', 'comments_count', 'interested_count',
            'join_request', 'image', 'image_filter',
            'profile_id', 'profile_image'
        ]

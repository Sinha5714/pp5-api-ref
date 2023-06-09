# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Event
from interested.models import Interested
from join.models import Join
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Events model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_pic.url'
    )
    comments_count = serializers.ReadOnlyField()
    interested_count = serializers.ReadOnlyField()
    join_request = serializers.ReadOnlyField()
    interested_id = serializers.SerializerMethodField()
    join_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

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

    def get_interested_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            interested = Interested.objects.filter(
                owner=user, event=obj
            ).first()
            return interested.id if interested else None
        return None

    def get_join_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            join = Join.objects.filter(
                owner=user, event=obj
            ).first()
            return join.id if join else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'is_owner', 'created_on', 'updated_on', 'title',
            'category', 'sub_category', 'event_start_date', 'event_end_date',
            'content', 'comments_count', 'interested_count', 'interested_id',
            'join_request', 'join_id', 'image', 'image_filter',
            'profile_id', 'profile_image',
        ]

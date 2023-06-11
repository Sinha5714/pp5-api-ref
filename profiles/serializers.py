from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    user = serializers.ReadOnlyField(source='user.username')
    country = CountryField()
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    events_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                user=user, followed=obj.user
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'is_owner', 'created_on', 'updated_on', 'name',
            'country', 'about_me', 'instagram_link', 'facebook_link',
            'phone_number', 'email', 'profile_pic', 'following_id',
            'events_count', 'followers_count', 'following_count',
        ]

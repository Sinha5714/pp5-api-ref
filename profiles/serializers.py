from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'created_on', 'updated_on', 'name',
            'about_me', 'instagram_link', 'facebook_link',
            'phone_number', 'email', 'profile_pic',
        ]

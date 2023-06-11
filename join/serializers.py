from rest_framework import serializers
from django.db import IntegrityError
from .models import Join


class JoinListSerializer(serializers.ModelSerializer):
    """
    Serializer for the Join model
    """
    user = serializers.ReadOnlyField(source='user.username')
    event_title = serializers.ReadOnlyField(source='event.title')

    class Meta:
        model = Join
        fields = [
            'id', 'user', 'reason', 'created_on',
            'event_title',
        ]

    def create(self, validated_data):
        """
        Validation to stop a user posting join request to the same event twice
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already sent joining request!'
            })

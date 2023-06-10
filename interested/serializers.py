from rest_framework import serializers
from .models import Interested
from django.db import IntegrityError


class InterestedSerializer(serializers.ModelSerializer):
    """
    Serializer for the Interested model
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Interested
        fields = [
            'id', 'user', 'created_on', 'event',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already shown interest!'
            })

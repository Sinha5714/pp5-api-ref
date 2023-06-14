# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers
from django.db import IntegrityError

# Internal:
from .models import Join
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class JoinSerializer(serializers.ModelSerializer):
    """
    Serializer for the Join model
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Join
        fields = [
            'id', 'user', 'created_on', 'name', 'email', 'event',
        ]

    def create(self, validated_data):
        """
        Validation to stop a user sending multiple join request
        to the same event twice
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already sent joining request!'
            })

from rest_framework import serializers
from my_profile.core.models import Email


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Email.objects.create(**validated_data)

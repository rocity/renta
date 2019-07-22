from rest_framework import serializers

from accounts.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """
    User Profile Serializer
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', )

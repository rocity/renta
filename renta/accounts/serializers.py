import django.contrib.auth.password_validation as validators
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """
    User Profile Serializer
    """

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', )


class SignUpSerializer(serializers.ModelSerializer):
    """
    Signup Serialzier
    """

    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'confirm_password', )

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password', None)

        if not self.partial and password and confirm_password:
            errors = dict()

            if password != confirm_password:
                raise serializers.ValidationError('Your passwords do not match.')

            try:
                validators.validate_password(password=password, user=self.instance)

            except serializers.ValidationError as error:
                errors['password'] = list(error.messages)

            if errors:
                raise serializers.ValidationError(errors)

        return attrs

    def save(self, **kwargs):
        if self.validated_data.get('password'):
            self.validated_data['password'] = make_password(self.validated_data.get('password'))
        elif 'password' in self.validated_data and not self.validated_data['password']:
            del self.validated_data['password']

        super(SignUpSerializer, self).save(**kwargs)

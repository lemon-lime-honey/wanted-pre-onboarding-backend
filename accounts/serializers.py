import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class SignupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
            )
        return user


    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError(_("Password must be longer than 7 letters."))


    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
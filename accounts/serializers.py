import re
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as s
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class TokenObtainPairSerializer(s):
    username_field = get_user_model().USERNAME_FIELD


    def validate_email(self, value):
        if not re.match(r'^.{1,}@.{1,}$', value):
            raise serializers.ValidationError(_('Enter a valid Email address'))
        return value


    def validate_password(self, value):
        if not re.match(r'^.{8,}', value):
            raise serializers.ValidationError(_('Password must be longer than 7 letters'))
        return value


class UserSerializer(serializers.ModelSerializer):
    username_field = get_user_model().USERNAME_FIELD

    def validate_email(self, value):
        if not re.match(r'^.{1,}@.{1,}$', value):
            raise serializers.ValidationError(_('Enter a valid Email address'))
        return value


    def validate_password(self, value):
        if not re.match(r'^.{8,}', value):
            raise serializers.ValidationError(_('Password must be longer than 7 letters'))
        return value


    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)
import re
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as s
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class TokenObtainPairSerializer(s):
    username_field = get_user_model().USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)
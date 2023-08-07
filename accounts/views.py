from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .serializers import *


class SignupAPIView(generics.GenericAPIView):
    serializer_class = SignupSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
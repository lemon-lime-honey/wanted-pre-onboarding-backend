from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination


    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy'):
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer


    def create(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        post = self.queryset.get(pk=pk)

        if request.user != post.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=post, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk):
        post = self.queryset.get(pk=pk)

        if request.user != post.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
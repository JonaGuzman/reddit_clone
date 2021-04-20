from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """ Class based view listing info"""
    queryset = Post.objects.all() # looking to pull from DB
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
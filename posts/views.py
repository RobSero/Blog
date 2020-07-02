from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.views import APIView
from posts.models import Post
from .serializers import PostSerializer, PopulatedPostSerializer


# ------------- GET ALL BLOG POSTS ---------------
class PostIndex(APIView):
  def get_posts(self):
    try:
      return Post.objects.all()
    except Post.DoesNotExist:
      return NotFound()


  def get(self,req):
    all_posts = Post.objects.all()
    serialized_posts = PopulatedPostSerializer(all_posts,many=True)
    return Response(serialized_posts.data, status=status.HTTP_200_OK)
  
  
  
  
# ------------- GET SINGLE BLOG POST ---------------
class PostDetails(APIView):
  def get_post(self,pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      return NotFound()


  def get(self,req,pk):
    post = self.get_post(pk)
    serialized_post = PopulatedPostSerializer(post)
    return Response(serialized_post.data, status=status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.views import APIView
from posts.models import Post
from .serializers import PostSerializer


# ------------- GET ALL BLOG POSTS ---------------
class PostIndex(APIView):
  def get_posts(self):
    try:
      return Post.objects.all()
    except Post.DoesNotExist:
      return NotFound()


  def get(self,req):
    print('HELLLLOOOOO')
    all_posts = Post.objects.all()
    serialized_posts = PostSerializer(all_posts,many=True)
    return Response(serialized_posts.data, status=status.HTTP_200_OK)
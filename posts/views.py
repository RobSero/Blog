
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.views import APIView
from posts.models import Post
from categories.models import Category
from .serializers import PostSerializer, PopulatedPostSerializer
import random


# ------------- GET ALL BLOG POSTS ---------------
class PostIndex(APIView):
  def get_posts(self):
    try:
      return Post.objects.all()
    except Post.DoesNotExist:
      return NotFound()


  def get(self,req):
    all_posts = self.get_posts()
    serialized_posts = PopulatedPostSerializer(all_posts,many=True)
    # return Response(serialized_posts.data, status=status.HTTP_200_OK)
    return render(req, 'posts/home.html')
  
  
  
  
# ------------- GET SINGLE BLOG POST ---------------
class PostDetails(APIView):
  def get_post(self,pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      return NotFound()

# get similar posts by category type
  def get_category_posts(self,pk):
    try:
      return Post.objects.filter(category__id=pk)
    except Post.DoesNotExist:
      return NotFound()


  def get(self,req,pk):
    # get post
    post = self.get_post(pk)
     # get categories of post
    categories = post.category.all()
    # get other posts by category ids (__in will filter them by the manytomanyfield)
    related_posts = Post.objects.filter(category__in=categories).filter(~Q(pk=post.id))
    print(related_posts)
    return render(req, 'posts/blogShow.html', {'post': post, 'recommendedPosts' : related_posts[:4]})
  
  


# ------------- GET RECOMMENDED BLOG POSTS ---------------
class RecommendedPosts(APIView):
  # get one post
  def get_post(self,pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      return NotFound()

# get similar posts by category type
  def get_category_posts(self,pk):
    try:
      return Post.objects.filter(category__id=pk)
    except Post.DoesNotExist:
      return NotFound()


  def get(self,req,pk):
    # get main post
    post = self.get_post(pk)
    # get categories of post
    categories = post.category.all()
    # get other posts by category ids (__in will filter them by the manytomanyfield)
    related_posts = Post.objects.filter(category__in=categories).filter(~Q(pk=post.id))
    # create a random selection
    # serialize and send
    serialized_recommended_posts = PopulatedPostSerializer(related_posts,many=True)
    if len(serialized_recommended_posts.data) > 5:
      random_selection = random.sample(serialized_recommended_posts.data, k=4)
      print(random_selection)
      return Response(random_selection, status=status.HTTP_200_OK)
    return Response(serialized_recommended_posts.data, status=status.HTTP_200_OK)
  
  

# ------------- GET ALL CATEGORY BLOG POSTS ---------------
class CategoryPosts(APIView):
  def get_category_posts(self,pk):
    try:
      return Post.objects.filter(category__id=pk)
    except Post.DoesNotExist:
      return NotFound()


  def get(self,req,pk):
    all_posts = self.get_category_posts(pk=pk)
    serialized_posts = PopulatedPostSerializer(all_posts,many=True)
    return Response(serialized_posts.data, status=status.HTTP_200_OK)
  

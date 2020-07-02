from rest_framework import serializers
from categories.serializers import CategorySerializer
from .models import Post



class PostSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Post
    fields = '__all__'
    

class PopulatedPostSerializer(PostSerializer):
  category = CategorySerializer(many=True)
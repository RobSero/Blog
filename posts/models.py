from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=250)
  main_image = models.CharField(max_length=300)
  sub_image = models.CharField(max_length=300)
  description = models.TextField(max_length=150)
  content_block_one = models.TextField(max_length=415)
  content_block_two = models.TextField(max_length=615)
  content_block_three = models.TextField(max_length=540)
  content_block_four = models.TextField()
  author = models.ForeignKey(
    User,
    related_name='author',
    on_delete=models.CASCADE,
    null=True
  )
  category = models.ManyToManyField(
    'categories.Category',
    related_name='post'
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'{self.id} - {self.title}'
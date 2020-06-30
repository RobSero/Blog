from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=250)
  image = models.CharField(max_length=300)
  content = models.TextField()
  author = models.ForeignKey(
    User,
    related_name='author',
    on_delete=models.CASCADE,
    null=True
  )
  category = models.ManyToManyField(
    'categories.Category',
    related_name='posts'
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'{self.id} - {self.title}'
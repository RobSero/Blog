from django.urls import path
from .views import PostIndex, PostDetails, CategoryPosts, RecommendedPosts

urlpatterns = [
    path('', PostIndex.as_view()),
    path('<int:pk>/', PostDetails.as_view()),
    path('category/<int:pk>/', CategoryPosts.as_view()),
    path('recommend/<int:pk>/', RecommendedPosts.as_view())
]

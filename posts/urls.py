from django.urls import path
from .views import PostIndex, PostDetails, CategoryPosts

urlpatterns = [
    path('', PostIndex.as_view()),
    path('<int:pk>/', PostDetails.as_view()),
    path('category/<int:pk>/', CategoryPosts.as_view() )
]

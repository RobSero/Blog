from django.urls import path
from .views import PostIndex, PostDetails

urlpatterns = [
    path('', PostIndex.as_view()),
    path('<int:pk>/', PostDetails.as_view()),
]

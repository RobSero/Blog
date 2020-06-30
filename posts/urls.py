from django.urls import path
from .views import PostIndex

urlpatterns = [
    path('', PostIndex.as_view())
]

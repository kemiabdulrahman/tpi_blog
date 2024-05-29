from django.contrib import admin
from django.urls import path
from blog.views import PostListCreate, PostDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/posts/', PostListCreate.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]


from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog_index/', views.BlogPostListView.as_view(), name='blog-index'),
]
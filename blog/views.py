from django.views.generic import ListView

from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost

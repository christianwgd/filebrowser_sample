from django.db import models
from filebrowser.fields import FileBrowseField
from tinymce.models import HTMLField


class BlogPost(models.Model):

    class Meta:
        verbose_name = "Blog post"
        verbose_name_plural = "Blog posts"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200, verbose_name="Title")
    image = FileBrowseField(
        verbose_name="Image", max_length=200,
        directory="images/", extensions=[".jpg", ".jpeg", ".png"],
        null=True, blank=True
    )
    content = HTMLField(verbose_name="Content", null=True, blank=True)
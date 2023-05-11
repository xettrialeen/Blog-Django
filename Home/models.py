from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')

    content = QuillField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class AboutPage(models.Model):
    short_title = models.CharField(max_length=200, blank=True)
    short_description = models.CharField(max_length=350, blank=True)

    profile_image = models.ImageField(upload_to='static/images/profile')
    long_description = QuillField(null=True)
    fb_link = models.URLField(blank=True)
    insta_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "About Page"

    def has_add_permission(self, request):
        # Return False to disable the "Add" button in the Django admin panel
        return not AboutPage.objects.exists()

    def __str__(self) -> str:
        return self.short_title


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

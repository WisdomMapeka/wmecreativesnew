from distutils.command.upload import upload
from django.db import models
from tinymce.models import HTMLField 


class Categories(models.Model):
    name = models.CharField(null=True, blank=True, max_length=300)
    icon = models.ImageField(upload_to="media_files/Categories/icon", null=True, blank=True)
    icon_class = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    category = models.ManyToManyField(Categories, blank=True)
    lead_img = models.ImageField(upload_to='media_files/blog', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    content = HTMLField()
    summary = models.TextField(null=True, blank=True, help_text="31 letters max will give a better out look")
    author = models.CharField(max_length=200, null=True, blank=True)
    author_image = models.ImageField(upload_to='media_files/authorImg', null=True, blank=True)
    youtube_video_link = models.TextField(null=True, blank=True)
    num_views = models.CharField(max_length=30, null=True, blank=True)
    read_time = models.CharField(max_length=30, null=True, blank=True)
    # styleshit = models.CharField(max_length=100, null=True, blank=True, choices=choices, default="shades-of-purple.min.css")
    


    def __str__(self):
        return self.title
    

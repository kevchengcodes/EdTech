from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.
class PostList(models.Model):
    def __str__(self):
        return self.Title
    Author = models.TextField()
    Body = models.TextField()
    PostDate = models.DateField(blank=True, null=True)
    Role = models.CharField(max_length=255)


class PostForm(ModelForm):
    class Meta:
        model = PostList
        fields = '__all__'

class ProjPostList(models.Model):
    def __str__(self):
        return self.Title
    Author = models.TextField()
    Body = models.TextField()
    PostDate = models.DateField(blank=True, null=True)
    Role = models.CharField(max_length=255)
    ProjKey = models.CharField(max_length=255)


class ProjPostForm(ModelForm):
    class Meta:
        model = ProjPostList
        fields = '__all__'

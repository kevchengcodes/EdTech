from django.db import models
from django.forms import ModelForm

# Create your models here.
class NewsList(models.Model):
    def __str__(self):
        return self.Title
    Title = models.TextField()
    Summary = models.TextField()
    Article = models.TextField()
    Image = models.TextField()
    Link = models.TextField()
    Date = models.TextField()

class ArticlesClicked(models.Model):
    def __str__(self):
        return self.Title
    Title = models.TextField()
    Summary = models.TextField()
    Article = models.TextField()
    Image = models.TextField()
    Link = models.TextField()
    Date = models.TextField()


class ArticlesClickedForm(ModelForm):
    class Meta:
        model = ArticlesClicked
        fields = '__all__'
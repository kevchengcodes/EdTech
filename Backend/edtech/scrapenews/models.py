from django.db import models

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
    
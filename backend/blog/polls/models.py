from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    article_id = models.IntegerField()

class Image(models.Model):
    url = models.CharField(max_length=100)
    img_id = models.IntegerField()
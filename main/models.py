from django.db import models

# Create your models here.

class Books(models.Model):
    bookName = models.CharField(max_length=200)
    bookDetails = models.CharField(max_length=1000)
    bookAmount = models.IntegerField(default=0)
    bookLink = models.URLField(blank=True)
    bookImage = models.FileField(default="")


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    fimage = models.FileField()
    posted = models.DateField(db_index=True, auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

from django.db import models
from django.urls import reverse

# Create your models here.
# class Topic(models.Model):
#     name= models.CharField(max_length=250)
#     description=models.TextField()

# class Author(models.Model):
#     name= models.CharField(max_length=200)
#     image=models.ImageField(upload_to="images/")
#     date= models.DateTimeField()
#     # topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
# class Comment(models.Model):
#     user= models.CharField(max_length=200)
#     content= models.TextField()  
      
class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime= models.DateTimeField()
    # author=models.ForeignKey(Author, on_delete=models.CASCADE)
    subtitle=models.TextField(default="null")
    body=models.TextField()
    image = models.ImageField(upload_to='upload/', default="null")
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    # comment=models.ForeignKey(Comment, on_delete=models.CASCADE)

class Galery(models.Model):
    title = models.CharField(max_length=255)
    datetime= models.DateTimeField()
    subtitle=models.TextField(default="null")
    body=models.TextField()
    image = models.ImageField(upload_to='upload/', default="null")


class Comment(models.Model):
    username = models.CharField(max_length=100)
    datetime= models.DateTimeField(auto_now=True)
    body=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
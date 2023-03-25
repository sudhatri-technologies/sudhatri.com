from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phoneNumber=models.IntegerField()
    message=models.TextField()

class Post(models.Model):
    title=models.CharField(max_length=500)
    slug=models.SlugField(max_length=500)
    date_added=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images/blogimages")
    body=models.TextField()
    

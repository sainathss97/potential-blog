from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime ,date
from ckeditor.fields import RichTextField 
# Create your models here.

choices = [('coding','coding'), ('food','food') , ('space','space')]
class Post(models.Model):
    title = models.CharField( max_length=500)
    title_tag = models.CharField( max_length=500,default  = 'Awesome Blog !')
    header_image = models.ImageField( upload_to='images/',null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    post_date = models.DateTimeField( auto_now=False, auto_now_add=True)
    cateogry = models.CharField( max_length=250,default='Coding')
    likes = models.ManyToManyField(User,related_name = 'blog_post')
    snippet = models.CharField( max_length=250,)
    
    
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + ' | By ->'  +str( self.author)

    def get_absolute_url(self):
        return reverse("index")
    

class Category(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")



class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = RichTextField()
    profile_pic = models.ImageField(null=True,blank =True, upload_to='profiles/', max_length=None)
    website_url = models.CharField(null= True,blank =True, max_length=500)
    facebook_url = models.CharField(null= True,blank =True, max_length=500)
    instagram_url = models.CharField(null= True,blank =True, max_length=500)
    other_url = models.CharField(null= True,blank =True, max_length=500)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("index")

class Comment(models.Model):

    post = models.ForeignKey(Post, related_name = 'comments' , on_delete=models.CASCADE)
    name = models.CharField( max_length=500)
    body = RichTextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=True)
  

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)


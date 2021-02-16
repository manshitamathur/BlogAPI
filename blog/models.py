from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    
    name = models.CharField(max_length=200,db_index=True)
    
    def __str__(self):
        return self.name



class BlogPost(models.Model):
    
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    blog_body = models.TextField()

    def __str__(self):
        return self.title





    

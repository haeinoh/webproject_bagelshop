from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestion(models.Model):
    suggestion = models.CharField(max_length=140)

    def __str__(self):
        return self.suggestion

class menu_post(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(max_length=144, upload_to='uploads/%Y/%m/%d/')
    price = mdoels.IntegerField()
    description = models.TextField()

class comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    comments = models.ManyToManyField(comment)

class custom_recipe(models.Model):
    title = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    comments = models.ManyToManyField(comment)
    image = models.ImageField(max_length=144, upload_to='uploads/%Y/%m/%d/')

class order_post(models.Model):
     author = models.ForeignKey(User, null=True,blank=True)
     menu=models.ForeignKey(menu_post)
     created=models.DataeTimeFiels(auto_new_add=True)

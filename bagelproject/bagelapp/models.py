from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestion(models.Model):
    suggestion = models.CharField(max_length=140)

    def __str__(self):
        return self.suggestion

class Product(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(max_length=144, upload_to='uploads/%Y/%m/%d/')
    price = models.IntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.name

class comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    comments = models.ManyToManyField(comment)

class Custom(models.Model):
    title = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    comments = models.ManyToManyField(comment)
    image = models.ImageField(max_length=144, upload_to='uploads/%Y/%m/%d/')

class Order(models.Model):
     author = models.ForeignKey(User, null=True, blank=True)
     product = models.ForeignKey(Product)
     timestamp = models.DataeTimeFiels(auto_new_add=True)

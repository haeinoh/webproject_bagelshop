from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
    suggestion = models.CharField(max_length=140)

    def __str__(self):
        return self.suggestion

class Product(models.Model):
    title = models.CharField(max_length=140)
    #image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    comments = models.ManyToManyField('Comment')

class Custom(models.Model):
    title = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    comments = models.ManyToManyField('Comment')
    #image = models.ImageField()

class Order(models.Model):
     author = models.ForeignKey(User, null=True, blank=True)
     product = models.ForeignKey(Product)
     timestamp = models.DateTimeField(auto_now_add=True)

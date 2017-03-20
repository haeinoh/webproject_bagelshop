from django.db import models

from django.contrib.auth.models import User

class Suggestion(models.Model):
    suggestion = models.CharField(max_length=140)

    def __str__(self):
        return self.suggestion

class Blog(models.Model):
    published_on=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=144)
    content=models.TextField()
    image=models.ImageField(max_length=144, upload_to='uploads/%Y/%m/%d/')
    image_description=models.CharField(max_length=144)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
class comment(models.Model):
    posted_on=models.DateTimeField(auto_now_add=True)
    comment_content=models.CharField(max_length=144)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,related_name="comments")
# Create your models here.

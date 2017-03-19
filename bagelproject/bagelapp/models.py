from django.db import models

from django.contrib.auth.models import User

class Suggestion(models.Model):
    suggestion = models.CharField(max_length=140)

    def __str__(self):
        return self.suggestion
# Create your models here.

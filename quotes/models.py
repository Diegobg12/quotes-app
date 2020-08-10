from django.db import models

# Create your models here.

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length = 200)# Set the max len of author in 200 characters

    def __str__(self):
        return self.text[:50]
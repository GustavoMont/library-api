from turtle import title
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    release_year = models.DateField()
    available = models.BooleanField(default=False)
    author = models.CharField(max_length=255)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.title
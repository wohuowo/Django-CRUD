#from turtle import title
from django.db import models

# Create your models here.
class TodoApp(models.Model):#model name
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title()


from django.db import models

# Create your models here.
class Joke(models.Model): #it inherits from models.Model
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): # this determines what gets output when a Joke instance is converted to a string
        return self.question
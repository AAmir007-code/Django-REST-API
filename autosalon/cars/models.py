from turtle import title
from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.model


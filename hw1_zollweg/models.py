from django.db import models


# Create your models here.

class Game(models.Model):
    name = models.TextField()
    genre = models.TextField()
    year = models.DateField()
    multiplayer = models.BooleanField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Developer(models.Model):
    dev_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Game(models.Model):
    game_title = models.CharField(max_length=200)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    time_to_beat = models.FloatField(default=0)
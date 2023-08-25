import datetime
from django.db import models

# Create your models here.
class Developer(models.Model):
    dev_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.dev_name

class Game(models.Model):
    game_title = models.CharField(max_length=200)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    time_to_beat = models.FloatField(default=0)
    release_date = models.DateField(default=datetime.date(1960, 1, 1))

    def __str__(self):
        return self.game_title
    
    def released_after_2000(self):
        return self.release_date.year > 2000
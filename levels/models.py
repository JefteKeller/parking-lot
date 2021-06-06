from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=150, unique=True)
    fill_priority = models.IntegerField()
    motorcycle_spaces = models.IntegerField()
    car_spaces = models.IntegerField()


class LevelSpace(models.Model):
    variety = models.CharField(max_length=150)
    level_name = models.CharField(max_length=150)

    level = models.ForeignKey(Level,
                              related_name='level_spaces',
                              on_delete=models.CASCADE)

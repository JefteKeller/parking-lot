from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=150)
    fill_priority = models.IntegerField()
    motorcycle_spaces = models.IntegerField()
    car_spaces = models.IntegerField()

    @classmethod
    def get_available_level_by_priority(cls, vehicle_type):
        all_levels = cls.objects.all().order_by('fill_priority')

        chosen_level = None
        for level in all_levels:
            level_capacity = level.car_spaces if vehicle_type == 'car' else level.motorcycle_spaces

            if level.level_spaces.filter(
                    variety=vehicle_type).count() < level_capacity:
                chosen_level = level
                break

        return chosen_level


class LevelSpace(models.Model):
    variety = models.CharField(max_length=150)
    level_name = models.CharField(max_length=150)

    level = models.ForeignKey(Level,
                              related_name='level_spaces',
                              on_delete=models.CASCADE)

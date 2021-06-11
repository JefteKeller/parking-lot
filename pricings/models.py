from django.db import models


class PricingManager(models.Manager):
    use_for_related_fields = True

    def get_latest_pricing(self):
        return self.last()


class Pricing(models.Model):
    a_coefficient = models.IntegerField()
    b_coefficient = models.IntegerField()

    objects = PricingManager()

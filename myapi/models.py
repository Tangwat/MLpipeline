from django.db import models
class Farmer(models.Model):
    name = models.CharField(max_length=60)
    farmNature = models.CharField(max_length=60)
    def __str__(self):
        return self.name

from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField

class PointOfInterest(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    location = models.PointField()
    category = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    ratings = ArrayField(models.IntegerField(), blank=True, null=True)

    class Meta:
        db_table = "points_of_interest"

    def __str__(self):
        return self.name
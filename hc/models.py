from django.db import models


class Sprint(models.Model):
    name = models.CharField(max_length=128)
    index = models.IntegerField(null=True, blank=True)
    totalPoints = models.IntegerField(null=True, blank=True)
    pointsMerged = models.IntegerField(null=True, blank=True)
    extraDeploys = models.IntegerField(null=True, blank=True)
    delayed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

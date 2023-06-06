from django.db import models


class Sprint(models.Model):
    name = models.CharField(max_length=128)
    index = models.IntegerField()

    def __str__(self):
        return self.name

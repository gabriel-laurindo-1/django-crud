from django.db import models

class MUSIC_MODEL(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    year = models.IntegerField()
    description = models.CharField(max_length=50, verbose_name='Description')

    def __str__(self):
        return f"{self.name}[{self.year}]: {self.description}"


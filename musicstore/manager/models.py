from django.db import models
from django.utils.timezone import now

class MUSIC_MODEL(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    year = models.IntegerField()
    description = models.CharField(max_length=50, null=True, verbose_name='Description')
    last_modification = models.DateTimeField(auto_now=True, null=True, verbose_name='Date Last Modification')

    def __str__(self):
        return f"{self.name}[{self.year}]: {self.description}"


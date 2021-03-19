from django.db import models
from django.utils.timezone import now

class MUSIC_MODEL(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    year = models.IntegerField()
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name='Description')
    last_modification = models.DateTimeField(auto_now=True, null=True, verbose_name='Date Last Modification')
    genre = models.ForeignKey('MUSIC_GENRE_MODEL', on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f"{self.name} [{self.year}]"

    class Meta:
        db_table = 'MUSIC'


class MUSIC_GENRE_MODEL(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name='Genre'
        )
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MUSIC_GENRE'

class ARTIST_MODEL(models.Model):

    name = models.CharField(max_length=20, verbose_name='Name')
    age = models.IntegerField()
    music = models.ForeignKey('MUSIC_MODEL', on_delete = models.CASCADE, null = True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ARTIST'
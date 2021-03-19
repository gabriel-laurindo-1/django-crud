from django import forms

from .models import *

class MusicModelForm(forms.ModelForm):
    class Meta:
        model = MUSIC_MODEL
        fields = '__all__'

class GenreModelForm(forms.ModelForm):
    class Meta:
        model = MUSIC_GENRE_MODEL
        fields = '__all__'

class ArtistModelForm(forms.ModelForm):
    class Meta:
        model = ARTIST_MODEL
        fields = '__all__'
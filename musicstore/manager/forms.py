from django import forms

from .models import *
from datetime import datetime

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

        widgets = {
            'age': forms.DateTimeInput(
                attrs={
                    'format':'yyyy-MM-ddThh:mm:ss',
                    'type': 'datetime-local',
                    'step': 1,
                    'require': False,
                    'placeholder': 'Write was born'
                }
            )
        }

    # Validação

    def clean_name(self):
        check = self.cleaned_data['name']
        if len(check) > 10:
            raise forms.ValidationError("Escolha uma opção válida.")
        return check


class AlbumForm1(forms.Form):
    name = forms.CharField(max_length=100)
    release_year = forms.IntegerField(min_value=1970, max_value=2021)
    production_year = forms.IntegerField(min_value=1970, max_value=2021)
    artist = forms.ModelChoiceField(queryset=ARTIST_MODEL.objects.all())

class AlbumForm2(forms.Form):
    genre = forms.ModelChoiceField(MUSIC_GENRE_MODEL.objects.all())

class AlbumForm3(forms.Form):
    music = forms.CharField(max_length=100, required=False)
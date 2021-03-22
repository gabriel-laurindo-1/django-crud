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

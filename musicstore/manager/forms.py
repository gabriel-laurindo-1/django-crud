from django import forms

from .models import *

class MusicModelForm(forms.ModelForm):
    class Meta:
        model = MUSIC_MODEL
        fields = '__all__'
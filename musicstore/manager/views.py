from django.shortcuts import render
from django.views.generic import CreateView


from .models import *
from .forms import MusicModelForm

# Create your views here.
class MusicCreateView(CreateView):
    
    model = MUSIC_MODEL
    template_name = 'home.html'
    fields = '__all__'
    
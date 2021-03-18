from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    DetailView, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


from .models import *
from .forms import MusicModelForm

# Create your views here.

class MusicListView(ListView):
    template_name = 'home.html'
    queryset = MUSIC_MODEL.objects.all()
    success_url = '/'

class MusicCreateView(CreateView):
    model = MUSIC_MODEL
    fields = '__all__'
    template_name = 'music_form.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class MusicUpdateView(UpdateView):
    model = MUSIC_MODEL
    fields = '__all__'
    template_name = 'music_form.html'
    success_url = '/'

    def get_object(self):
        _id = self.kwargs.get('pk')
        return get_object_or_404(self.model, id=_id)

    def form_valid(self, form):
        return super().form_valid(form)

class MusicDeleteView(DeleteView):
    model = MUSIC_MODEL
    template_name = 'music_delete.html'
    
    def get_object(self):
        slug_pk = self.kwargs.get("pk")
        return get_object_or_404(self.model, pk=slug_pk)

    def get_success_url(self):
        return reverse('manager:music-list')
    
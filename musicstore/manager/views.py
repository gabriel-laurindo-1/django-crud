from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    DetailView, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from formtools.wizard.views import SessionWizardView

from .models import *
from .forms import *

# Create your views here.

class MusicDetailView(DetailView):
    model = MUSIC_MODEL
    fields = '__all__'
    template_name = 'music_detail.html'
    success_url = '/'

    def get_object(self):
        _id = self.kwargs.get('pk')
        return get_object_or_404(self.model, id=_id)


class MusicListView(ListView):
    template_name = 'home.html'
    queryset = MUSIC_MODEL.objects.all()
    success_url = '/'

class MusicCreateView(CreateView):
    model = MUSIC_MODEL
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageName'] = 'Music Register'
        return context


class MusicUpdateView(UpdateView):
    model = MUSIC_MODEL
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = '/'

    def get_object(self):
        _id = self.kwargs.get('pk')
        return get_object_or_404(self.model, id=_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageName'] = 'Music Update'
        return context

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
    

class GenreCreateView(CreateView):
    model = MUSIC_GENRE_MODEL
    fields = '__all__'
    template_name = 'model_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageName'] = 'Genre Register'
        return context


class ArtistCreateView(CreateView):
    model = ARTIST_MODEL
    form_class = ArtistModelForm
    template_name = 'model_form.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageName'] = 'Artirst Register'
        return context
    
class ArtistDetailView(DetailView):
    model = ARTIST_MODEL
    fields = '__all__'
    template_name = 'artist_detail.html'
    success_url = '/'

    def get_object(self):
        _id = self.kwargs.get('pk')
        return get_object_or_404(self.model, id=_id)

class ArtistListView(ListView):
    template_name = 'artist_list.html'
    queryset = ARTIST_MODEL.objects.all()
    success_url = '/'

class ArtistUpdateView(UpdateView):
    model = ARTIST_MODEL
    form_class = ArtistModelForm
    template_name = 'model_form.html'
    success_url = '/'

    def get_object(self):
        _id = self.kwargs.get('pk')
        return get_object_or_404(self.model, id=_id)

    def get_initial(self):
        initial = super().get_initial()

        # retrieve current object
        default_format_datetime_local_html5 = self.object.age.strftime('%Y-%m-%dT%H:%M:%S')
        initial['age'] = default_format_datetime_local_html5

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageName'] = 'Artist Update'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class ArtistDeleteView(DeleteView):
    model = ARTIST_MODEL
    template_name = 'music_delete.html'
    
    def get_object(self):
        slug_pk = self.kwargs.get("pk")
        return get_object_or_404(self.model, pk=slug_pk)

    def get_success_url(self):
        return reverse('manager:artist-list')


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    return form_data

def show_message_form_condition(wizard):
    # try to get the cleaned data of step 1
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    # check if the field ``leave_message`` was checked.
    print('show_message_form_condition:', cleaned_data.get('production_year', True))
    return cleaned_data.get('production_year', True)

class AlbumWizard(SessionWizardView):
    template_name = 'contact.html'
    success_url = 'contact.html'
    form_list = [AlbumForm1, AlbumForm2, AlbumForm3]


    def get_form_step_data(self, form):
        return form.data

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        context['state_form'] = 'Welcome'

        # print('self.steps.current:', self.steps.current, type(self.steps.current))

        if self.steps.current == '1':
            context.update(
                {
                    'state_form': 'WVT'
                })
        return context

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)

        return render(self.request, template_name='done.html', context={'form_data': form_data})


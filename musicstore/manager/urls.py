
from django.urls import path
from .views import (
    MusicDetailView,
    MusicListView,
    MusicCreateView,
    MusicUpdateView,
    MusicDeleteView,
    GenreCreateView,
    ArtistDetailView,
    ArtistListView,
    ArtistCreateView,
    ArtistUpdateView,
    ArtistDeleteView,
    AlbumWizard,
    show_message_form_condition
)

app_name = 'manager'
urlpatterns = [
    path('', MusicListView.as_view(), name="music-list"),
    path('create/', MusicCreateView.as_view(), name="music-create"),
    path('detail/<int:pk>', MusicDetailView.as_view(), name="music-detail"),
    path('update/<int:pk>', MusicUpdateView.as_view(), name="music-update"),
    path('delete/<int:pk>', MusicDeleteView.as_view(), name="music-delete"),
    path('create-genre/', GenreCreateView.as_view(), name="genre-create"),
    path('artist-create/', ArtistCreateView.as_view(), name="artist-create"),
    path('artist/', ArtistListView.as_view(), name="artist-list"),
    path('artist/<int:pk>', MusicDetailView.as_view(), name="artist-detail"),
    path('artist-update/<int:pk>', ArtistUpdateView.as_view(), name="artist-update"),
    path('artist-delete/<int:pk>', ArtistDeleteView.as_view(), name="artist-delete"),
    path('album/', AlbumWizard.as_view(condition_dict={'1': show_message_form_condition}), name='album'),
]
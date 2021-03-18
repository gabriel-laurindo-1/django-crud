
from django.urls import path
from .views import (
    MusicDetailView,
    MusicListView,
    MusicCreateView,
    MusicUpdateView,
    MusicDeleteView
)

app_name = 'manager'
urlpatterns = [
    path('', MusicListView.as_view(), name="music-list"),
    path('create/', MusicCreateView.as_view(), name="music-create"),
    path('detail/<int:pk>', MusicDetailView.as_view(), name="music-detail"),
    path('update/<int:pk>', MusicUpdateView.as_view(), name="music-update"),
    path('delete/<int:pk>', MusicDeleteView.as_view(), name="music-delete"),
]
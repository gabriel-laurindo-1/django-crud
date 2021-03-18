
from django.urls import path
from .views import MusicCreateView

app_name = 'manager'
urlpatterns = [
    path('create/', MusicCreateView.as_view(), name="music-create"),
]
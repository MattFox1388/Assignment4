from django.urls import path
from .views import AddArtist,AddSong,ViewSongs

urlpatterns = [
    path('', ViewSongs.as_view()),
    path('add_artist', AddArtist.as_view()),
    path('add_song', AddSong.as_view())
]
from django.shortcuts import render
from .models import Artist,Song
from django.views import View
# Create your views here.

class ViewSongs(View):
    def get(self, request):
        return render(request, 'view_songs.html', {})
    def post(self, request):
        pass
class AddSong(View):
    def get(self, request):
        return render(request, 'enter_song.html', {})
    def post(self, request):
        pass
class AddArtist(View):
    def get(self, request):
        return render(request, 'enter_artist.html', {})
    def post(self, request):
        pass


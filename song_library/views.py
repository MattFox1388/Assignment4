from django.shortcuts import render
from .models import Artist,Song
from django.views import View
from .forms import ViewForm, ArtistForm, SongForm
# Create your views here.

class ViewSongs(View):
    def get(self, request):
        form = ViewForm()
        return render(request, 'view_songs.html', {'form':form, 'name':''})
    def post(self, request):
        form = ViewForm(request.POST)
        if form.is_valid():
            #process data
            songList,name = form.process()
        form = ViewForm()
        return render(request,'view_songs.html',{'form':form,'song_list':songList,'name':name})

class AddSong(View):
    def get(self, request):
        form = SongForm('Pick Artist','Type Song')
        return render(request, 'enter_song.html', {'form':form})
    def post(self, request):
        form = SongForm('Pick Artist','Type Song',request.POST)
        if form.is_valid():
            form.process()
        form = SongForm('Pick Artist','Type Song')
        return render(request,'enter_song.html',{
            'form':form
        })

class AddArtist(View):
    def get(self, request):
        form = ArtistForm()
        artistList = Artist.objects.all()
        return render(request, 'enter_artist.html', {'form':form,'artist_list':artistList})
    def post(self, request):
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.process()
        artistList = Artist.objects.all()
        form = ArtistForm()
        return render(request,'enter_artist.html',{'form':form,'artist_list':artistList})


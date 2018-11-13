from django import forms
from .models import Artist,Song
#forms below
class ViewForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Artist.objects.all())

    def process(self):
        artistSelected = self.cleaned_data['choice']
        songList = Song.objects.filter(artist=artistSelected)
        return songList, artistSelected.name

class ArtistForm(forms.Form):
    createArtist = forms.CharField(label='Enter New Artist',max_length=30)

    def process(self):
        artistTyped = self.cleaned_data['createArtist']
        Artist.objects.create(name=artistTyped)

class SongForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Artist.objects.all())
    songSelect = forms.CharField(max_length=30)

    def process(self):
        artistSelected = self.cleaned_data['choice']
        songSelected = self.cleaned_data['songSelect']
        Song.objects.create(title=songSelected,artist=artistSelected)

    def __init__(self,firstLabel, secondLabel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['choice'].label = firstLabel
        self.fields['songSelect'].label = secondLabel

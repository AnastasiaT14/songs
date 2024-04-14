from django import forms
from .models import SongWriter, Song

class SongWriterForm(forms.ModelForm):
    class Meta:
        model = SongWriter
        fields = ['name', 'surname', 'picture', 'bio']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'song_writer', 'genre', 'release_date']

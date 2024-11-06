# myapp/forms.py
from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['playlist_name']  # Adjust this to include other fields if needed

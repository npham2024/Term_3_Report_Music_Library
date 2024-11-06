from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.http import HttpResponse

from .forms import PlaylistForm
from .models import Playlist, Song, PlaylistSong


def home(request):
    return HttpResponse("<h1>Welcome to My Basic Django Webpage</h1>")


# def album_list(request):
#     playlists = Playlist.objects.all()
#
#     return render(request, 'album_list.html', {'playlists': playlists})


def home_view(request):
    playlists = Playlist.objects.all()  # Fetch all playlists
    return render(request, 'home.html', {'playlists': playlists})


def playlist_detail_view(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    song_ids = PlaylistSong.objects.filter(playlist_id=playlist_id).values_list('song_id', flat=True)
    songs = Song.objects.filter(song_id__in=song_ids)  # Songs in the playlist
    all_songs = Song.objects.exclude(song_id__in=song_ids)  # Songs not in the playlist
    return render(request, 'playlist_detail.html', {
        'playlist': playlist,
        'songs': songs,
        'all_songs': all_songs
    })


def add_song_to_playlist(request, playlist_id):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        playlist = get_object_or_404(Playlist, pk=playlist_id)
        song = get_object_or_404(Song, pk=song_id)

        if not PlaylistSong.objects.filter(playlist_id=playlist.playlist_id, song_id=song.song_id).exists():
            PlaylistSong.objects.create(playlist_id=playlist.playlist_id, song_id=song.song_id)

        return redirect('playlist_detail', playlist_id=playlist.playlist_id)


def remove_song_from_playlist(request, playlist_id, song_id):
    # Remove the song from the playlist
    PlaylistSong.objects.filter(playlist_id=playlist_id, song_id=song_id).delete()
    return redirect('playlist_detail', playlist_id=playlist_id)


def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlaylistForm()
    return render(request, 'create_playlist.html', {'form': form})


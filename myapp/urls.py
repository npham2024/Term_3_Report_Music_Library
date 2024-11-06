# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page shows all playlists
    path('playlist/<int:playlist_id>/', views.playlist_detail_view, name='playlist_detail'),  # Playlist detail page
    path('playlist/<int:playlist_id>/add_song/', views.add_song_to_playlist, name='add_song_to_playlist'),  # Add song
    path('playlist/<int:playlist_id>/remove_song/<int:song_id>/', views.remove_song_from_playlist, name='remove_song_from_playlist'),  # Remove song
    path('playlist/create/', views.create_playlist, name='create_playlist')  # Playlist creation page

]

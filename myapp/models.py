# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=255)
    artist_id = models.IntegerField()

    class Meta:
        db_table = 'Album'
        managed = False


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Artist'
        managed = False


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    playlist_name = models.CharField(max_length=255)
    created_date = models.DateField()
    user_id = models.IntegerField()

    class Meta:
        db_table = 'Playlist'
        managed = False


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    artist_id = models.IntegerField()
    album_id = models.IntegerField()

    class Meta:
        db_table = 'Song'
        managed = False


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'User'
        managed = False

    def __str__(self):
        return self.username


class PlaylistSong(models.Model):
    id = models.AutoField(primary_key=True)
    playlist_id = models.IntegerField()
    song_id = models.IntegerField()

    class Meta:
        db_table = 'Playlist_Song'
        managed = False
        unique_together = (('playlist_id', 'song_id'),)

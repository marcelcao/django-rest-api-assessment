from django.db import models
from .genre import Genre
from .song import Song

class SongGenre(models.Model):

    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="genre_songs")
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="song_genres")

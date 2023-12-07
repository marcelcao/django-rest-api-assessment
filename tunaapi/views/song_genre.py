"""View module for handling requests about songs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Genre, SongGenre
from tunaapi.serializers import SongGenreSerializer

class SongGenreView(ViewSet):
  """Song Genre View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single song genre"""
    
    try:
      song_genre = SongGenre.objects.get(pk=pk)
      serializer = SongGenreSerializer(song_genre)
      return Response(serializer.data)
    except SongGenre.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET for all song genre"""
    
    song_genre = SongGenre.objects.all()
      
    serializer = SongGenreSerializer(song_genre, many=True)
    return Response(serializer.data)

  def create(self, request):
    """Handles POST song genre"""
    
    song = Song.objects.get(pk=request.data["song_id"])
    genre = Genre.objects.get(pk=request.date["genre_id"])
    
    song_genre = SongGenre.objects.create(
      song_id=song,
      genre_id=genre,
    )
    serializer = SongGenreSerializer(song)
    return Response(serializer.data)
    
  def update(self, request, pk):
    """Handles PUT request for song genre"""
    
    song_genre = SongGenre.objects.get(pk=pk)
    
    song = Song.objects.get(pk=request.data["song_id"])
    genre = Genre.objects.get(pk=request.data["genre_id"])
    
    song_genre.song_id = song
    song_genre.genre_id = genre
    
    song_genre.save()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    """Handles Delete request for song genre"""
    
    song_genre = SongGenre.objects.get(pk=pk)
    song_genre.delete()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)

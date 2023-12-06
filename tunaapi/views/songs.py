"""View module for handling requests about songs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist, SongGenre

class SongView(ViewSet):
  """Song View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single song"""
    
    try:
      song = Song.objects.get(pk=pk)
      serializer = SongSerializer(song)
      return Response(serializer.data)
    except Song.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET for all songs"""
    
    songs = Song.objects.all()
    
    song_artist = request.query_params.get('artist_id', None)
    if song_artist is not None:
      song = song.filter(song_artist_id=song_artist)
      
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

  def create(self, request):
    """Handles POST song"""
    
    song_artist = Artist.objects.get(pk=request.data["artist_id"])
    
    song = Song.objects.create(
      title=request.data["title"],
      artist_id=song_artist,
      album=request.data["album"],
      length=request.data["length"],
    )
    serializer = SongSerializer(song)
    return Response(serializer.data)
    
  def update(self, request, pk):
    """Handles PUT request for song"""
    
    song = Song.objects.get(pk=pk)
    song.title = request.data["title"]
    song.album = request.data["album"]
    song.length = request.data["length"]
    
    song_artist = Artist.objects.get(pk=request.data["artist_id"])
    song.artist_id = song_artist
    song.save()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    """Handles Delete request for song"""
    
    song = Song.objects.get(pk=pk)
    song.delete()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)

class SongGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongGenre
        fields = ('genre_id', )
        depth = 1
    
class SongSerializer(serializers.ModelSerializer):
  """JSON serializer for songs"""
  
  genres = SongGenreSerializer(many=True, read_only=True)
  
  class Meta:
    model = Song
    fields = ('id', 'title', 'artist_id', 'album', 'length', 'genres')
    depth = 1

    
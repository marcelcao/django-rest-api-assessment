"""View module for handling requests about artists"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist, Song
from tunaapi.serializers import SongSerializer
from django.db.models import Count

class ArtistView(ViewSet):
  """Artist View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single artist"""
    
    try:
      artist = Artist.objects.annotate(song_count=Count('songs')).get(pk=pk)
      serializer = ArtistSongsSerializer(artist)
      return Response(serializer.data)
    except Artist.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET for all artists"""
    
    artists = Artist.objects.all()
      
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

  def create(self, request):
    """Handles POST artist"""
    
    artist = Artist.objects.create(
      name=request.data["name"],
      age=request.data["age"],
      bio=request.data["bio"],
    )
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)
    
  def update(self, request, pk):
    """Handles PUT request for artist"""
    
    artist = Artist.objects.get(pk=pk)
    artist.name = request.data["name"]
    artist.age= request.data["age"]
    artist.bio = request.data["bio"]

    artist.save()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    """Handles Delete request for artist"""
    
    artist = Artist.objects.get(pk=pk)
    artist.delete()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)

class ArtistSongsSerializer(serializers.ModelSerializer):
  """JSON serializer to get artist's associated songs"""
  songs = SongSerializer(many=True, read_only=True)
  song_count = serializers.IntegerField(default=None)
  
  class Meta:
    model = Artist
    fields = ('id', 'name', 'age', 'bio', 'song_count', 'songs', )
    depth = 1
class ArtistSerializer(serializers.ModelSerializer):
  """JSON serializer for artists"""
  class Meta:
    model = Artist
    fields = ('id', 'name', 'age', 'bio')
    depth = 0

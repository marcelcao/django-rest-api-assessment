from rest_framework import serializers
from tunaapi.models import Song

class SongArtistSerializer(serializers.ModelSerializer):
  """JSON serializer for single song"""
  class Meta:
    model = Song
    fields = ('id', 'title', 'album', 'length', )
    depth = 0

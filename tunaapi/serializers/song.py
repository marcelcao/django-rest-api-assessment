from rest_framework import serializers
from tunaapi.models import Song

class SongSerializer(serializers.ModelSerializer):
  """JSON serializer for all songs"""
  class Meta:
    model = Song
    fields = ('id', 'title', 'artist_id', 'album', 'length', )
    depth = 0

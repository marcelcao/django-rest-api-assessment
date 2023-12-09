from rest_framework import serializers
from tunaapi.models import Genre

class GenreSerializer(serializers.ModelSerializer):
  """JSON serializer for artists"""
  class Meta:
    model = Genre
    fields = ('id', 'description',)
    depth = 1

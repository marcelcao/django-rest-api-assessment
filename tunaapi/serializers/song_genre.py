from rest_framework import serializers
from tunaapi.models import SongGenre

class SongGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongGenre
        fields = ('genre_id', )
        depth = 1

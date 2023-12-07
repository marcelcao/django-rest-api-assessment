from rest_framework import serializers
from tunaapi.models import SongGenre

class GenreSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongGenre
        fields = ('song_id', )
        depth = 1

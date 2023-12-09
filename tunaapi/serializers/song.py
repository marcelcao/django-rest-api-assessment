from rest_framework import serializers
from tunaapi.models import Song

class SongSerializer(serializers.ModelSerializer):
  """JSON serializer for all songs"""
  class Meta:
    model = Song
    fields = ('id', 'title', 'artist_id', 'album', 'length', )
    depth = 0

  def __init__(self, *args, **kwargs):
    # Don't pass the 'fields' arg up to the superclass
    fields = kwargs.pop('fields', None)

    # Instantiate the superclass normally
    super().__init__(*args, **kwargs)

    if fields is not None:
        # Drop any fields that are not specified in the `fields` argument.
        allowed = set(fields)
        existing = set(self.fields)
        for field_name in existing - allowed:
            self.fields.pop(field_name)

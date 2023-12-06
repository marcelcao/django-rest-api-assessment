"""View module for handling requests about artists"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre

class GenreView(ViewSet):
  """Genre View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single genre"""
    
    try:
      genre = Genre.objects.get(pk=pk)
      serializer = GenreSerializer(genre)
      return Response(serializer.data)
    except Genre.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET for all genres"""
    
    genres = Genre.objects.all()
      
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

  def create(self, request):
    """Handles POST genre"""
    
    genre = Genre.objects.create(
      description=request.data["description"],
    )
    serializer = GenreSerializer(genre)
    return Response(serializer.data)
    
  def update(self, request, pk):
    """Handles PUT request for genre"""
    
    genre = Genre.objects.get(pk=pk)
    genre.description = request.data["description"]

    genre.save()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    """Handles Delete request for genre"""
    
    genre = Genre.objects.get(pk=pk)
    genre.delete()
    
    return Response (None, status=status.HTTP_204_NO_CONTENT)
class GenreSerializer(serializers.ModelSerializer):
  """JSON serializer for artists"""
  class Meta:
    model = Genre
    fields = ('id', 'description',)
    depth = 1

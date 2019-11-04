from rest_framework import serializers
from .models import Movie

class movie_serializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # fields = ('inq_nam', 'inq_mono')
        fields = '__all__'
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import movie_serializer
import boto3

DYNAMODB = boto3.resource('dynamodb')
TABLE = DYNAMODB.Table('transcript_tbl')

class all_movie(APIView):
    tbl_scan = TABLE.scan()
    all_user = tbl_scan['Items']
    print(all_user)
    def get(self, request):
        all_mov = Movie.objects.all()
        serilizer = movie_serializer(all_mov, many=True)
        return Response(serilizer.data)
    def post(self):
        pass


# Create your views here.


def index(request):
    return render(request, 'api/index.html')

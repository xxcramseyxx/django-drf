from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializer
from .models import Moviedata

# Create your views here.


class MovieViewSets(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = Movieserializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='action')
    serializer_class = Movieserializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='comedy')
    serializer_class = Movieserializer

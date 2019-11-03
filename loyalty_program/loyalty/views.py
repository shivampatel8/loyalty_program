from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import Person
from .serializers import PersonSerializer
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HelloView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

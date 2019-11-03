from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from django.contrib.auth.models import User, Group
from rest_framework import viewsets


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

# @api_view([..])

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class HelloView(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

@permission_classes((permissions.AllowAny,))
class HelloView1(APIView):
    def get(self, request):
      queryset = Person.objects.all()
      print (queryset)
      serializer_class = PersonSerializer
      content = {'message': 'Hello, World!'}
      return Response(content)



class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        return Response(content)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def person_detail(request):
    """
    Retrieve, update or delete a code snippet.
    """
    
    uname = request.GET['uname']
    try:
        snippet = Person.objects.get(username=uname)
        return Response(status=status.HTTP_200_OK)   
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)        
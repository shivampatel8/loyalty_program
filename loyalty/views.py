from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Person,Points
from .serializers import PersonSerializer,PointSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.core import serializers

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

import json
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


@permission_classes((permissions.AllowAny,))
class GetPoints(APIView):
    def get(self,request,format=None):
        queryset = Points.objects.all()
        queryset1 = Person.objects.all()
        print(queryset)
        print(queryset1)
        owner = request.GET['username']
        print(owner)
        uid = Person.objects.filter(username= owner).values("user_id")[0]["user_id"]
        print(uid)
        if owner is not None:
            #queryset = Points.objects.filter(username=owner)
            #print(queryset.query)
            #print(Points.objects.select_related('owner_id'))
            #a = Points.objects.filter(owner_id_id__user_id=uid)
            #print(a.query)
            queryset = queryset.filter(owner_id=int(uid))
            print(queryset)
            output_list = []
            for i in queryset:
                print(i.reciever_id.username)
                output_list.append({'receiver':i.reciever_id.username,'points':i.points})
            print(output_list)
            #a = Person.objects.raw('SELECT * FROM myapp_person inner join myapp_points using myapp_person.user_id = myapp_points.owner_id' )
            #print(a)
        print('points')
        print(PointSerializer(queryset))
        print('queryset')
        print(queryset)
        print('json serializer')
        print(serializers.serialize('json',queryset))
        #return Response(serializers.serialize('json',queryset))
        json_str = json. dumps(output_list)
        return Response(json_str)

@permission_classes((permissions.AllowAny,))
class AllPoints(APIView):
    def get(self,request,format=None):
        queryset = Points.objects.all()
        queryset1 = Person.objects.all()
        owner = request.GET['username']
        uid = Person.objects.filter(username= owner).values("user_id")[0]["user_id"]
        if owner is not None:
            queryset = queryset.filter(owner_id=int(uid))
        print(PointSerializer(queryset))
        return Response(serializers.serialize('json',queryset))

@permission_classes((permissions.AllowAny,))
class AddPoints(APIView):
    def get(self,request,format=None):
        queryset = Points.objects.all()
        queryset1 = Person.objects.all()
        owner = request.GET['username']
        licker = request.GET['licker']
        points = request.GET['points']
        uid = Person.objects.filter(username= owner).values("user_id")[0]["user_id"]
        lid = Person.objects.filter(username= licker).values("user_id")[0]["user_id"]
        try:
            t = Points.objects.get(owner_id=uid,reciever_id=lid)
            x = int(t.points)
            x +=int(points)
            t.points = x
            t.save()
        except Exception as e:
            u = Person(user_id = uid)
            l = Person(user_id = lid)
            p = Points(owner_id=u,reciever_id=l,points=points)
            p.save()
        return Response(serializers.serialize('json',queryset))



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
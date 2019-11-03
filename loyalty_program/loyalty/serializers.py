from rest_framework import serializers
from .models import Person,Points


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("user_id", "username", "password")


class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Points
        fields = ("owner_id","reciever_id","points")
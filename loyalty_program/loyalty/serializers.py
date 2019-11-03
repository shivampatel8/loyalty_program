from rest_framework import serializers
from .models import Person


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("user_id", "username", "password")

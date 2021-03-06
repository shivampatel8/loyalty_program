from django.db import models
from django import forms


# Create your models here.


class Person(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)





class Points(models.Model):
    owner_id = models.ForeignKey(Person,related_name="owner_id",on_delete = models.CASCADE)
    reciever_id = models.ForeignKey(Person,related_name="reciever_id",on_delete=models.CASCADE)
    points = models.CharField(max_length=30)


    class Meta:
        unique_together = (('owner_id', 'reciever_id'))

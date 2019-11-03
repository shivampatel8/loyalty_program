from django.db import models
from django import forms

# Create your models here.


class person(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

	class Meta:
		model = User


class points(models.Model):
	owner_id = models.ForeignKey(Person, primary_key=True)
  reciever_id = models.ForeignKey(Person, primary_key=True)
  points = models.CharField(max_length=30)

  class Meta:
  	unique_together = (('owner_id', 'reciever_id'))

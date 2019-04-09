from django.db import models

# Create your models here.
class Animal(models.Model):
	animaltype = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	age = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	class Meta:
		db_table: "animal"

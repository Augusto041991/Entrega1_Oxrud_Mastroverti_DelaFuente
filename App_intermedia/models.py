from django.db import models

# Create your models here.
class Ventas(models.Model):

    nombre= models.CharField(max_length=30)
    sueldo = models.IntegerField()
    email= models.EmailField()


class Contabilidad(models.Model):
    nombre= models.CharField(max_length=30)
    sueldo = models.IntegerField()
    email= models.EmailField()

class Produccion(models.Model):
    nombre= models.CharField(max_length=30)
    sueldo = models.IntegerField()
    email= models.EmailField()



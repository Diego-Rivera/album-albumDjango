from datetime import datetime
from time import timezone
from django.db import models

# Create your models here.
class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True)
    nombreFoto = models.CharField(max_length=100)
    nombreArchivo= models.CharField(max_length=256)
    descripcion=models.CharField(max_length=500)
    fechaPublicacion=models.DateField(default=datetime.now())

    def __str__(self):
        return self.nombreFoto
        
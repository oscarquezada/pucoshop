from django.db import models
from django.utils import timezone

class Producto(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    imagen= models.ImageField(null=True ,blank=True)
        
    
    def __str__(self):
        return self.title   
    
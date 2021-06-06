from django.db import models
from django.utils import timezone
from django import forms


class Cliente (models.Model):
       

    Rut = models.CharField(max_length=10)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'12345678-9'}))
    Nombres=models.CharField(max_length=50)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'Juan Perez'}))
    clave= models.CharField(max_length=50 , null=True )


    Correo=models.EmailField( max_length=50)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'Ejemplo@Ejemplo.com'}))
    Telefono=models.CharField(max_length=50)
                            #widget= forms.TextInput
                            #(attrs={'placeholder':'987654321'}))


    def __str__(self):
        return self.Rut
        

class Producto(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    imagen= models.ImageField(null=True ,blank=True)
        
    
    def __str__(self):
        return self.title   
    
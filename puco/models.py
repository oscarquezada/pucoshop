from typing import Text
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields.files import ImageField



class Cliente (AbstractBaseUser):
       

    rut = models.CharField(max_length=10, unique=True)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'12345678-9'}))
    nikename=models.CharField(max_length=10,unique=True)                       
    nombres=models.CharField(max_length=50)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'Juan Perez'}))
    password= models.CharField(max_length=50 , null=False )


    correo=models.EmailField( max_length=50)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'Ejemplo@Ejemplo.com'}))
    telefono=models.CharField(max_length=50)
                            #widget= forms.TextInput
                            #(attrs={'placeholder':'987654321'}))
    last_login= models.DateTimeField(null=True)
                           
    USERNAME_FIELD='nikename'
    def __str__(self):
        return self.nikename
        
        

class Producto(models.Model):
    Tipos = (
        ('P','Perro'),
        ('G','Gato'),
    )
    Tamano=(
        ('P','Pequeño'),
        ('M','Mediano'),
        ('G','Grande'),
    )
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=50)
    precio = models.IntegerField(max_length=10)
    imagen= models.ImageField(null=True ,blank=True)
    cantidad=models.IntegerField(max_length=10)
    tipo= models.CharField(max_length=1, choices=Tipos)
    
    tamano=models.CharField(max_length=1, choices=Tamano)

        
    
    def __str__(self):
        return self.title   
class Ofertas(models.Model):
    title=models.CharField(max_length=200)     
    Text=models.CharField(max_length=50)
    precio=models.IntegerField(max_length=10)
    imagen=models.ImageField(null=True,blank=True)   
   
    def __str__(self):
        return self.title

    
class Mascota(models.Model):
    Tipos = (
        ('P','Perro'),
        ('G','Gato'),
    )
    Tamano=(
        ('P','Pequeño'),
        ('M','Mediano'),
        ('G','Grande'),
    )

    rut=models.CharField(max_length=10)
    tipo= models.CharField(max_length=1, choices=Tipos)
    edad = models.CharField(max_length=2)
    tamano=models.CharField(max_length=1, choices=Tamano)
    peso=models.CharField(max_length=2)
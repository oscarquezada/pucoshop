from django.db import models
from django.contrib.auth.models import AbstractBaseUser



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
        return self.rut
        

class Producto(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    imagen= models.ImageField(null=True ,blank=True)
        
    
    def __str__(self):
        return self.title   
    
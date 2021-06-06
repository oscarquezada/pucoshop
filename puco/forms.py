from django import forms
from django.db.models import fields

from .models import Producto,Cliente



class PostForm(forms.ModelForm):
    clave=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
        fields = ('Rut', 'Nombres','clave','Correo','Telefono')  
          
class LoginPostForm(forms.ModelForm):    
    clave=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
        fields = ('Nombres','clave')
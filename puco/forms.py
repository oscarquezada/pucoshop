from django import forms
from django.db.models import fields

from .models import Producto,Cliente,Mascota



class PostForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
        fields = ('rut', 'nombres','nikename','password','correo','telefono')  
          
class LoginPostForm(forms.ModelForm):    
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
        fields = ('nikename','password')

class MascotaPostForm(forms.ModelForm):
    class Meta:
        model= Mascota
        fields = ('rut','tipo','edad','tamano','peso')
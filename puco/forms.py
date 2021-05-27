'''from django import forms

from .models import Consulta,Producto


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Consulta
        fields = ('Rut', 'Nombres','Correo','Telefono','Asunto')'''
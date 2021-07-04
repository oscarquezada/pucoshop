from django.contrib import admin
from .models import Ofertas, Producto,Cliente,Mascota
# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Ofertas)
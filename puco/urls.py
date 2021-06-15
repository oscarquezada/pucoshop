from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.producto, name='principal'),
    
    path('welcome', views.welcome,name='welcome'),


    #path de los loguin

    path('register', views.register),
    path('login', views.login_user),
    path('logout', views.logout),
    path('carrito/agregar', views.agregarCarro)
]


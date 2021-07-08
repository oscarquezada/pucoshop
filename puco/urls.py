from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include




urlpatterns = [
    path('', views.productoMuestra, name='principal'),
 
    path('welcome', views.productos ,name='welcome'),
    path('recomendaciones', views.recomendaciones ,name='recomendaciones'),


    path('register', views.register),
    path('login', views.login_user),
    path('logout', views.logout),
    path('mascota', views.mascota),
    path('carrito', views.carrito),
    
    path('agregarProductoCarro', views.agregarProductoCarro),
    path('agregarOfertaCarro', views.agregarOfertaCarro),
    path('eliminarProductoCarro', views.eliminarProductoCarro),
    path('eliminarOfertaCarro', views.eliminarOfertaCarro),
    path('menosProductoCarro', views.menosProductoCarro),
    path('menosOfertaCarro', views.menosOfertaCarro),
    path('eliminarCarro', views.eliminarCarro),
]


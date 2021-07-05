from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.productoMuestra, name='principal'),
 
    path('welcome', views.productos ,name='welcome'),
    path('recomendaciones', views.recomendaciones ,name='recomendaciones'),
    


    #path de los loguin

    path('register', views.register),
    path('login', views.login_user),
    path('logout', views.logout),
    path('mascota', views.mascota),
    path('carrito', views.carrito),
    path('agregarProductoCarro', views.agregarProductoCarro),
    path('eliminarProductoCarro', views.eliminarProductoCarro),
    path('menosProductoCarro', views.menosProductoCarro),
    path('eliminarCarro', views.eliminarCarro),
]


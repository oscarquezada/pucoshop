from django.utils import timezone
from .models import Producto

from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def producto(request):
    producto=Producto.objects.all()
    return render(request, 'puco/principal.html', {"producto":producto}) 

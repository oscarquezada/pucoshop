from django.utils import timezone
from .models import Cliente,Producto
from .forms import PostForm ,LoginPostForm
from django.contrib.auth import backends, logout as do_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.views.defaults import page_not_found
from .backend import MyBackend

# Create your views here.

myBakend=MyBackend()

 
def mi_error_404(request, exception):
    return render(request,'puco/404.html',{'error':exception})
    #return page_not_found(request, template_name=nombre_template)

    
def producto(request):
    producto=Producto.objects.all()
    ultimos=Producto.objects.order_by('-id')[:4]
    return render(request, 'puco/principal.html', {"producto":producto,"ultimos":ultimos}) 


def register(request):
    # Creamos el formulario de autenticación vacío
    form = PostForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = PostForm(request.POST)     

        if form.is_valid():
            form.save()  
            # Creamos la nueva cuenta de usuario

            # Si el usuario se crea correctamente 
            if form is not None:
                # Hacemos el login manualmente
                # Y le redireccionamos a la portada
                return redirect('/login')

    # Si llegamos al final renderizamos el formulario
    return render(request, "puco/register.html", {'form': form})

def login_user(request):
    # Creamos el formulario de autenticación vacío
    
    form = LoginPostForm()
    if request.method == "POST":
        print("llegue al post")
        # Añadimos los datos recibidos al formulario
        form = LoginPostForm(data=request.POST)
        # Si el formulario es válido...
            # Recuperamos las credenciales validadas
        rut = form['nikename'].value()
        clave = form['password'].value()
        print(rut)
            #Ejemplo
        user=myBakend.authenticate(request,username=rut,password=clave)
           
           
        if user is not None:
            login(request,user,backend='puco.backend.MyBackend')
            return redirect('welcome')
            

    # Si llegamos al final renderizamos el formulario
    return render(request, "puco/login.html", {'form': form})



def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def welcome(request):
    
    return render(request, 'puco/welcome.html')



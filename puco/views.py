from django.utils import timezone
from .models import Cliente,Producto
from .forms import PostForm ,LoginPostForm
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
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

def login(request):
    # Creamos el formulario de autenticación vacío
    form = LoginPostForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = LoginPostForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            Nombres = form.cleaned_data['Nombres']
            clave = form.cleaned_data['clave']

            #Ejemplo
            print(Nombres)
            # Verificamos las credenciales del usuario
            #cliente = authenticate(Nombres=Nombres, clave=clave)
            #print(cliente)
            # Si existe un usuario con ese nombre y contraseña
            if Cliente.objects.filter(Nombres=Nombres, clave=clave).exists():#cliente is not None:
                # Hacemos el login manualmente
                #do_login(request, cliente)
                # Y le redireccionamos a la portada
                return redirect('/welcome',{'Nombres':Nombres})

    # Si llegamos al final renderizamos el formulario
    return render(request, "puco/login.html", {'form': form})



def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def welcome(request):
    return render(request, 'puco/welcome.html')
    #pro=Postproducto()
    #if request.Cliente.is_authenticated:
    #    return render(request, "puco/welcome.html",{
    #        #'pro',pro
    #        })
    #return redirect('/login')
'''def post_pro(request):
    if request.method == "POST":
        pro = Postproducto(request.POST)
        if pro.is_valid():
            post = pro.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        pro = Postproducto()
    return render(request, 'puco/welcome.html', {'pro': pro})      '''
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')   
        
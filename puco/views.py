from django.utils import timezone
from .models import Cliente,Producto, Mascota
from .forms import PostForm ,LoginPostForm, MascotaPostForm
from django.contrib.auth import backends, logout as do_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.views.defaults import page_not_found
from .backend import MyBackend
from .cart import Cart

# Create your views here.
myBakend=MyBackend()
def carrito(request):
    carrito=Cart(request)
    return render(request,'puco/carrito.html', {"carrito":carrito.cart.items(), "total":carrito.total})


def agregarProductoCarro(request):
    
    carrito=Cart(request)
    id=request.GET['id']
    productoDB= Producto.objects.get(pk=id)
    
    producto={"id":id, "nombre":productoDB.title,"precio":productoDB.precio}
    carrito.add(producto)
    print(carrito)
    print(carrito.total)
    return redirect('welcome')
   

def eliminarProductoCarro(request):
    #id recuperar id
    carrito=Cart(request)
    productoDb= Producto.objects.get(pk=id)
    
    producto={"id":id, "nombre":productoDb.nombre,"precio":productoDb.precio}

    carrito.remove(producto)
    return redirect('pucoshop/carrito')

def menosProductoCarro(request):
    
    carrito=Cart(request)
    producotDb=Producto.objects.get(pk=id)
    producto={"id":id, "nombre":producotDb.nombre,"precio":producotDb.precio}

    carrito.decrement(producto)
    return redirect('/')
def eliminarCarro(request):
    carrito=Cart(request)
    producotDb=Producto.objects.get(pk=id)
    producto={"id":id, "nombre":producotDb.nombre,"precio":producotDb.precio}

    carrito.clear(producto)
    return redirect('/')



 
def mi_error_404(request, exception):
    return render(request,'puco/404.html',{'error':exception})
    #return page_not_found(request, template_name=nombre_template)

    
def productoMuestra(request):
    
    ultimos=Producto.objects.order_by('-id')[:4]
    return render(request, 'puco/principal.html', {"ultimos":ultimos}) 

def producto(request):
    producto=Producto.objects.all()
    return render(request,'puco/welcome.html',{"producto":producto})

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

def mascota(request):
    form = MascotaPostForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = MascotaPostForm(request.POST)     

        if form.is_valid():
            
            form.save()  
            # Creamos la nueva cuenta de usuario

            # Si el usuario se crea correctamente 
            if form is not None:
                # Hacemos el login manualmente
                # Y le redireccionamos a la portada
                return redirect('/welcome')

    return render(request, 'puco/mascota.html', {'form': form})



def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
class Cart:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        cart=self.session.get("cart")
        if not cart:
            cart=self.session["cart"]={}
        self.cart=cart
        total=self.session.get("total")
        if not total:
            total=self.session["total"]=0
        self.total=total
        total=self.session.get("total")

    def calcular(self):        
        for key,value in self.cart.items():
            #print(value["cantidad"])
            self.total=self.total+(int(value["precio"])*int(value["cantidad"]))
            self.save()

        
    def add(self,producto):
        if str(producto.get("id")) not in self.cart.keys():
            self.cart[producto.get("id")]={
            "producto_id":producto.get("id"),
            "nombre":producto.get("nombre"),
            "cantidad":1,
            "precio":str(producto.get("precio")),
            "subTotal":producto.get("precio")*1
            }
            
        else:
            for key,value in self.cart.items():
                if key == str(producto.get("id")):
                    value["cantidad"]=value["cantidad"]+1
                    value["subTotal"]=int(value["cantidad"])* int(value["precio"])
                    break
            
        print(self.cart)
        self.save()
        self.calcular()

    def save(self):
        self.session["cart"]=self.cart
        self.session["total"]=self.total
        self.session.modified =True

        
    def remove(self,producto):
        producto_id=str(producto.get("id"))
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
        self.calcular()



    def decrement(self,producto):
        for key,value in self.cart.items():
            
            if key ==str(producto.get("id")):
                value["cantidad"]=value["cantidad"]-1
                value["subTotal"]=int(value["cantidad"])* int(value["precio"])
                if value["cantidad"]<1:
                    self.remove(producto)  
                    
                    break  
                else:
                    self.save()
                
            else:
                print("el producto no existe en el carrito de compra")   
        self.calcular()                     
    def clear(self):
        self.session["cart"]={}
        self.session.modified=True
        self.total=0

        #oferta
    def add1(self,ofertas):
        if str(ofertas.get("id")) not in self.cart.keys():
            self.cart[ofertas.get("id")]={
            "oferta_id":ofertas.get("id"),
            "nombre":ofertas.get("nombre"),
            "cantidad":1,
            "precio":str(ofertas.get("precio")),
            "subTotal":ofertas.get("precio")*1
            }
            
        else:
            for key,value in self.cart.items():
                if key == str(ofertas.get("id")):
                    value["cantidad"]=value["cantidad"]+1
                    value["subTotal"]=int(value["cantidad"])* int(value["precio"])
                    break
            
        print(self.cart)
        self.save()
        self.calcular()

    def remove1(self,ofertas):
        ofertas_id=str(ofertas.get("id"))
        if ofertas_id in self.cart:
            del self.cart[ofertas_id]
        self.save()
        self.calcular()



    def decrement1(self,ofertas):
        for key,value in self.cart.items():
            
            if key ==str(ofertas.get("id")):
                value["cantidad"]=value["cantidad"]-1
                value["subTotal"]=int(value["cantidad"])* int(value["precio"])
                if value["cantidad"]<1:
                    self.remove(ofertas)  
                    
                    break  
                else:
                    self.save()
                
            else:
                print("la oferta no existe en el carrito de compra")   
        self.calcular()                     
    def clear(self):
        self.session["cart"]={}
        self.session.modified=True
        self.total=0

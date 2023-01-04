# -*- coding: utf-8 -*-

class Pelicula():
    def __init__(self, titulo = " ", duracion = 0.0, productor = " "):
        self.__titulo = titulo
        self.__duracion = duracion
        self.__productor = productor
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    @property
    def productor(self):
        return self.__productor
    
    @productor.setter
    def productor(self, productor):
        self.__productor = productor
    
    def __str__(self):
        resp = '\t Titulo: ' + self.titulo + '\n'
        resp = resp +'\t Duracion: ' + str(self.__duracion) + '\n'
        resp = resp +'\t Productor : ' + self.productor + '\n'
        return resp



    def Captura(self):
        self.titulo = input("--------------Pelicula-------------\nTitulo: ")
        self.__duracion = int(input("Duracion: "))
        self.__productor = input("Productor: ")
            
        


from Cliente import Cliente

class BoletoCine():
    def __init__(self, valorBoleto = 0.0, impuestoVenta = 0.0, cliente = Cliente(), pelicula = Pelicula() ):
        self.__valorBoleto = valorBoleto
        self.__impuestoVenta = impuestoVenta
        self.__cliente = cliente
        self.__pelicula = pelicula
        
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    
    @property
    def pelicula(self):
        return self.__pelicula
    
    @pelicula.setter
    def pelicula(self, pelicula):
        self.__pelicula = pelicula
        
    @property
    def valorBoleto(self):
        return self.__valorBoleto
    
    @valorBoleto.setter
    def valorBoleto(self, valorBoleto):
        self.__valorBoleto = valorBoleto
        
    @property
    def impuestoVenta(self):
        return self.__impuestoVenta
    
    @impuestoVenta.setter
    def impuestoVenta(self, impuestoVenta):
        self.__impuestoVenta = impuestoVenta
        
        

    def __str__(self):
        resp = '\t Cliente \n' + str(self.cliente)
        resp += '\t Pelicula \n' + str(self.pelicula)
        
            
        resp += '\n\t ValorBoleto: ' + str(self.valorBoleto) 
        resp += "\n\t ImpuestoVenta: " + str(self.impuestoVenta)
        resp += "\n\t Total a pagar con IVA : " +str (self.PrecioPagar())
        return resp
    
    def Captura(self):
        self.cliente.Captura()
        self.pelicula.Captura()
        self.valorBoleto = float(input("valorBoleto: "))
        self.impuestoVenta = float(input("ImpuestoVenta: "))
        
    
    def PrecioPagar(self):
        return self.valorBoleto + self.impuestoVenta 
    
    
    
    
class BoletoClienteFrecuente(BoletoCine):
    def __init__(self,  valorBoleto = 0.0, impuestoVenta = 0.0, cliente = Cliente(), pelicula = Pelicula(), descuento = 0.0 ):
        super().__init__( valorBoleto, impuestoVenta, cliente, pelicula)
        self.__descuento = descuento

    @property
    def descuento(self):
        return self.__descuento

    @descuento.setter
    def descuento(self, descuento):
        self.__descuento = descuento
    
    def __str__(self):
            resp = "\n--------------------Boleto Cliente Frecuente-------------------\n"
            resp += super().__str__()
            resp += '\n \t Descuento: ' + str(self.descuento) + ' \n'
            #resp += "\n\t Total a pagar más impuestos: " +str (self.PrecioPagar())
            resp += "\n--------------------------------------------------------\n"
            return resp
        
    def Captura(self):
        super().Captura()
        self.descuento = float(input("Porcentaje de Descuento: "))


    def PrecioPagar(self):
        return (self.valorBoleto + self.impuestoVenta)-((self.descuento/100) * self.valorBoleto)
    
    
    
    
class AlimentoExtra():
    def __init__(self, codigo = " ", descripcion = " ", precio = 0.0):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
    
    def __str__(self):
        resp = '\t Codigo: ' + self.codigo + '\n'
        resp = resp +'\t Descripcion: ' + self.__descripcion + '\n'
        resp = resp +'\t Precio : ' + str(self.precio) + '\n'
        return resp

    def Captura(self):
        self.codigo = input("--------------AlimentoExtra-------------\nCodigo: ")
        self.__descripcion = (input("Descripcion: "))
        self.precio = float(input("Precio: "))  
        
        
    
        
class BoletoEjecutivo(BoletoCine):
    def __init__(self,  valorBoleto = 0.0, impuestoVenta = 0.0, cliente = Cliente(), pelicula = Pelicula(), alimentos = [] ):
        super().__init__( valorBoleto, impuestoVenta, cliente, pelicula)
        self.__alimentos = alimentos

    @property
    def alimentos(self):
        return self.__alimentos

    @alimentos.setter
    def alimentos(self, alimentos):
        self.__alimentos = alimentos
    
    def __str__(self):
            resp = "\n--------------------Boleto Cliente Ejecutivo-------------------\n"
            resp += super().__str__()
            resp += "\n\n \t Alimentos: " 
            for i in range(len(self.alimentos)):
                resp += "\n"+ str(self.alimentos[i])
            resp += "\n--------------------------------------------------------\n"
            return resp
        
    def Captura(self):
        super().Captura()
        numAli = int(input("Numero de Alimentos: "))
        for i in range(numAli):
            aliEx = AlimentoExtra()
            aliEx.Captura()
            self.alimentos.append(aliEx)
        
    def totalAlimento(self):
       total = 0.0
       for i in range(len(self.alimentos)):
            total = total + self.alimentos[i].precio
       return total
   

    def PrecioPagar(self):
        return self.valorBoleto + self.impuestoVenta + self.totalAlimento()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""
p = Pelicula("PARASITE",120,"Yi Mu Hon")

#print(h.__str__())

c = Cliente("Andres","Heredia","71805598")

a1 = AlimentoExtra("4h5dd","Galletas",100)
a2 = AlimentoExtra("5h6dd","Pasta",100)

#print(c.__str__())

#b = BoletoCine(100,50,c,p)

ali = [a1, a2]

bF = BoletoClienteFrecuente(100,50,c,p,20)
bE = BoletoEjecutivo(100,50,c,p,ali)

#print(bF.__str__())
#print(bE.__str__())
#print(a1.__str__())
#print(a2.__str__())

"""
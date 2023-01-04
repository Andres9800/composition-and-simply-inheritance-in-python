# -*- coding: utf-8 -*-
from Base import Base

class Cliente(Base):
    def __init__(self, nombre="" , direccion = "", telefono = ""):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, nuevo_valor):
        self.__direccion = nuevo_valor
   
    def __str__(self):
        resp = '\t Nombre: ' + self.nombre + '\n'
        resp = resp +'\t Dirección: ' + self.direccion+'\n'
        resp = resp +'\t Telefono: ' + self.telefono+'\n'
        return resp
    
    def Captura(self):
        self.nombre = input("Nombre del cliente: ")
        self.direccion = input("Direccion del cliente: ")
        self.telefono = input("Telefono del cliente: ")
        
        

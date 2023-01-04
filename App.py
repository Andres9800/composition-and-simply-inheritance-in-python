from Lectura import Lectura
import os

class App:
    def __init__(self):
        self.__lista = list()
        self.__lec = Lectura()
    def __menu(self):
        #os.system('clear') #os.system('cls') #en windows
        print(" ==================================================== ")
        print(" [1] Insertar BoletoEjecutivo")
        print(" [2] Insertar BoletoClienteFrecuente ")
        print(" [3] Ver la lista de Boletos" )
        print(" [4] Borrar la lista de Boletos")
        print(" [5] Salir")
        print(" ==================================================== ")
        return input("> ")
    
    def __mostrarLista(self):
        os.system ("cls") 
        for i in range(len(self.__lista)):
            print(self.__lista[i])
          

    def principal(self):
        respuesta = ""
        while respuesta != "5":
            respuesta = self.__menu()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosBoletoEjecutivo())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosBoletoClienteFrecuente())
            elif respuesta == "3":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar")
            elif respuesta == "4":
                self.__lista.clear()

prueba = App()
prueba.principal()



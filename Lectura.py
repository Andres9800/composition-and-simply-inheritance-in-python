from BoletoCine import BoletoCine,BoletoEjecutivo, BoletoClienteFrecuente
import os
from Cliente import Cliente

class Lectura():
    def LeeDatosBoletoCine(self):
        boletoCine = BoletoCine()
        os.system('cls') 
        boletoCine.Captura()
        return boletoCine
    def LeeDatosBoletoEjecutivo(self):
        boletoEjecutivo = BoletoEjecutivo()
        os.system('cls') 
        boletoEjecutivo.Captura()
        return boletoEjecutivo
    def LeeDatosBoletoClienteFrecuente(self):
        boletoClienteFrecuente = BoletoClienteFrecuente()
        os.system('cls')
        boletoClienteFrecuente.Captura()
        return boletoClienteFrecuente
    




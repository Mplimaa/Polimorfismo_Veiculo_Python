from typing import override
from Veiculo import Veiculo

# Classe filha (subclasse)
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas=portas
    
    @override #notação p/ informar uso do metodo da classe mãe acelerar()
    def acelerar(self):
        # Implementação específica para Carro
        print(f"O carro {self.marca} {self.modelo} está acelerando suavemente.")

    def passear (self):#metodo da classe
        if self.portas >= 2:
             print(f"O carro com {self.portas} portas, facilita para a família maior")
        else:
            print(f"O carro com {self.portas} portas, paciência!!!")

    @override 
    def calcular_tempo_entrega(self,distancia):
        return distancia / 60 #vel. media 60km/h





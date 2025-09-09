from typing import override
from Veiculo import Veiculo

# Outra classe filha
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)    
        self.cilindradas=cilindradas

    @override    
    def acelerar(self):#notação p/ informar uso do metodo da classe mãe acelerar()
        # Implementação específica para Moto
        print(f"A moto {self.marca} {self.modelo} está acelerando com um ronco forte!")


    def empinar_moto(self):#metodo da classe
        if self.cilindradas >= 500:
            print("Uau! A moto tem potência de sobra para empinar!")
        else:
            print("Essa moto precisa de técnica do motociclista p/ empinar.")

    @classmethod
    def calcular_tempo_entrega(self,distancia):
        return distancia / 100 #vel. media 100km/h


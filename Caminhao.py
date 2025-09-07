from typing import override
from Veiculo import Veiculo

# Mais uma classe filha
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, eixos):
        super().__init__(marca, modelo)    
        self.eixos=eixos

    @override #notação p/ informar uso do metodo da classe mãe acelerar()
    def acelerar(self):
        # Implementação específica para Caminhão
        print(f"O caminhão {self.marca} {self.modelo} está acelerando lentamente, ganhando força.")

    def carregar_mercadoria(self):#metodo exclusivo da classe caminhao
        if self.eixos >= 8:
            print(f"O caminhão tem {self.eixos} eixos para transportar cargas de grande peso")
        else:
            print(f"O caminhão tem {self.eixos} eixos pode não suportar de cargas de grande peso")

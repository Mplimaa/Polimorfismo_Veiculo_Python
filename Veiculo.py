from abc import ABC, abstractmethod
#abc = Abstract Base Classes (Módulo interno do Python).
#ABC → transforma a classe em abstrata (não pode ser instanciada).
# abstractmethod → marca métodos que devem ser implementados pelas classes filhas.


# Classe mãe (superclasse)
class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        # Implementação genérica
        print("O veículo está acelerando de forma genérica.")
    
    #metodo abstrato obriga as classes filhas implementar, só pode ser feito nas filhas
    #cls = a própria classe que chamou o método naquele momento  // pass instrucao que nao faz nada
    @abstractmethod
    def calcular_tempo_entrega(self,distancia):
        pass




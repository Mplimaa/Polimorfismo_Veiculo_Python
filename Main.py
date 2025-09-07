from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto
from Caminhao import Caminhao

meu_carro = Carro("Ford", "Mustang", portas=4)
minha_moto = Moto("Honda", "CBR 600", cilindradas=599)
meu_caminhao = Caminhao("Scania", "R 450", eixos=8)

# Lista de veículos
veiculos = [meu_carro, minha_moto, meu_caminhao]

# Iterando sobre a lista e chamando o mesmo método para todos
for veiculo in veiculos:
    veiculo.acelerar()

meu_carro.passear()
minha_moto.empinar_moto()
meu_caminhao.carregar_mercadoria()
Este repositório, demonstra o conceito de polimorfismo na Programação Orientada a Objetos (POO).
O polimorfismo permite que classes diferentes (Carro, Moto e Caminhão) tenham o mesmo método (acelerar), mas com comportamentos diferentes.



### Estrutura dos Arquivos ##

Veiculo.py → Classe mãe (superclasse).

Carro.py → Classe filha que herda de Veiculo.

Moto.py → Classe filha que herda de Veiculo.

Caminhao.py → Classe filha que herda de Veiculo.

Main.py → Arquivo principal que cria os objetos e executa os métodos.



### Explicação das Classes ##

Veiculo (superclasse, classe mãe)
Classe genérica de onde os outros veículos herdam.
Define o método acelerar(), que é sobrescrito nas subclasses.


Carro (subclasse)
Herda de Veiculo.
Tem o atributo portas.
Sobrescreve o método acelerar() com comportamento específico.
Possui método extra passear()


Moto (subclasse)
Herda de Veiculo.
Tem o atributo cilindradas.
Sobrescreve o método acelerar().
Possui método extra empinar_moto().


Caminhao (subclasse)
Herda de Veiculo.
Tem o atributo eixos.
Sobrescreve o método acelerar().
Possui método extra carregar_mercadoria().



No arquivo principal para realizar as validações/testes do retorno, que eu chamei de Main.py, temos:


-- Lista de veículos
veiculos = [meu_carro, minha_moto, meu_caminhao]

-- Todos chamam o mesmo método acelerar()
for veiculo in veiculos:
    veiculo.acelerar()




Mesmo usando o mesmo método (acelerar), cada classe executa de forma diferente:

O carro acelera suavemente.
A moto acelera com ronco forte.
O caminhão acelera lentamente, ganhando força.



### Saída esperada ##


Ao executar Main.py, o resultado será algo assim:

O carro Ford Mustang está acelerando suavemente.
A moto Honda CBR 600 está acelerando com um ronco forte!
O caminhão Scania R 450 está acelerando lentamente, ganhando força.
O carro com 4 portas, facilita para a família maior
Uau! A moto tem potência de sobra para empinar!
O caminhão tem 8 eixos para transportar cargas de grande peso


### Conclusão ##

Este exemplo mostra de forma simples:

Herança (classes filhas herdando de Veiculo).

Polimorfismo (mesmo método com comportamentos diferentes).

Métodos específicos de cada classe.


###  Importante:::::::::::::::::::::::::: ##
O decorador Override, acontece quando uma classe filha redefine um método da classe mãe. Ou seja, a classe filha “sobrescreve” o comportamento original
do método. Isso é útil quando você quer que a classe filha faça algo diferente da classe mãe, mas mantendo a mesma interface (mesmo nome do método).

Em Python, não é obrigatório o uso, porque é uma linguagem dinâmica e flexível. O interpretador decide em tempo de execução qual método chamar, com 
base na hierarquia de classes e no objeto que está sendo usado. Mas, se quiser que o código fique mais claro e seguro pode usar o decorador @override,
importando a blibioteca typing.

Isso é polimorfismo: um mesmo método, vários comportamentos.


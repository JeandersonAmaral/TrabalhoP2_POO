'''Neste exemplo, a classe Carro herda da classe Veiculo.
Isso significa que o carro tem acesso ao método acelerar() a classe Veiculo sem precisar defini-lo novamente.
Além disso, a classe Carro também pode ter seus próprios métodos, como o método abrir_porta().'''

class Veiculo:
    def acelerar(self):
        print("O veículo está acelerando.")

class Carro(Veiculo):
    def abrir_porta(self):
        print("A porta do carro está aberta.")

'''Podemos criar um objeto da classe Carroe acessar seus métodos:'''

meu_carro = Carro()
meu_carro.acelerar()     # Saída: O veículo está acelerando.
meu_carro.abrir_porta()  # Saída: A porta do carro está aberta.

'''Assim, a herança permite que a classe derivada aproveite o código da classe base,
evitando duplicação e adicionando funcionalidades específicas, se necessário.'''
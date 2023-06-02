'''Nesse exemplo, temos uma classe Carro com um atributo _ cor e um método _ ligar_motor.
Esses elementos são considerados protegidos, pois têm um único sublinhado no início de seus nomes.
O método acelerar e os métodos obter_cor e alterar_cor são públicos e fornecem uma interface para
interagir com os atributos.'''

class Carro:
    def __init__(self):
        self._cor = 'vermelho'    # Atributo protegido com um sublinhado

    def _ligar_motor(self):       # Método protegido com um sublinhado
        print("Motor ligado.")

    def acelerar(self):
        self._ligar_motor()
        print("Acelerando o carro.")

    def obter_cor(self):
        return self._cor

    def alterar_cor(self, nova_cor):
        self._cor = nova_cor
        
'''Podemos criar um objeto da classe Carroe utilizar uma interface pública:'''

meu_carro = Carro()
meu_carro.acelerar()              # Saída: Motor ligado. Acelerando o carro.
print(meu_carro.obter_cor())      # Saída: vermelho
meu_carro.alterar_cor('azul')
print(meu_carro.obter_cor())      # Saída: azul

'''Observe que acessamos o atributo _ cor somente através dos métodos obter_core alterar_cor.
Essa é uma forma de aplicar o encapsulamento em Python, mesmo que o acesso aos atributos protegidos não seja restrito.'''
'''Nesse exemplo, temos a classe base Animal e três classes derivadas: Cachorro, Gato e Vaca.
Cada uma dessas classes possui um método fazer_som()que representa o som que o animal faz.'''

class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

class Vaca(Animal):
    def fazer_som(self):
        print("Moo!")


'''Agora, podemos criar objetos dessas classes e chamar o método fazer_som()em cada um deles:'''

cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

cachorro.fazer_som()  # Saída: Au au!
gato.fazer_som()     # Saída: Miau!
vaca.fazer_som()     # Saída: Moo!

'''Neste caso, cada objeto de uma classe específica (cachorro, gato, vaca) possui seu próprio método fazer_som(),
que é chamado de acordo com o tipo do objeto. Isso também é um exemplo de polimorfismo, pois objetos diferentes
têm comportamento diferente, mas são tratados de forma uniforme através da classe base Animal.'''

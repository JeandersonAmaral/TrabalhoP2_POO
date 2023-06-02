[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)
# Curso de Engenharia de Software 
[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2021/12/Simbolo_Engenharia_de_Software.jpg)](https://universidadedevassouras.edu.br/graduacao-marica/engenharia-de-software/)

### Desenvolvido pelo aluno do 3º Periodo, turma B:

* [Jeanderson Amaral](https://github.com/JeandersonAmaral)


### Disciplina:
* Laboratório de Programação Orientada a Objetos

### Professor:
* Fabrício Dias

## Enunciado
Criar um repositório no github, com as seguintes informações:

- O que é Polimorfismo e um exemplo de código usando polimorfismo
- O que é Herança e um exemplo de código usando herança
- O que é encapsulamento e um exemplo de código usando encapsulamento

Os exemplos dos códigos deverão ser feitos na linguagem de programação python.

<strong>OBS:</strong> Crie um README.md com o propósito do trabalho, com a explicação dos três tópicos. Em seguida, crie um arquivo em python para cada exemplo. Lembre de comentar o código para saber qual conceito está sendo tratada ali.

<hr>

# Polimorfismo:
O polimorfismo é um princípio na programação orientada a objetos que permite tratar objetos de classes diferentes de forma uniforme, mesmo que tenham comportamentos diferentes. Isso é alcançado através de hierarquias de classes, onde objetos de uma classe base podem ser referenciados por um tipo genérico e, em tempo de execução, o comportamento específico do objeto derivado é invocado. Existem dois tipos principais de polimorfismo: o de sobrecarga, que envolve várias funções com o mesmo nome mas com parâmetros diferentes, e de sobreposição, que ocorre quando uma classe derivada implementa um método de uma classe base. O polimorfismo torna o código mais flexível, reutilizável e modular, permitindo adicionar novas funcionalidades sem modificar o código existente.
### Exemplo:
Nesse exemplo, temos a classe base Animal e três classes derivadas: Cachorro, Gato e Vaca.
Cada uma dessas classes possui um método fazer_som()que representa o som que o animal faz.
```python
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
```
Agora, podemos criar objetos dessas classes e chamar o método fazer_som()em cada um deles:
```python
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

cachorro.fazer_som()  # Saída: Au au!
gato.fazer_som()     # Saída: Miau!
vaca.fazer_som()     # Saída: Moo!
```
Neste caso, cada objeto de uma classe específica (cachorro, gato, vaca) possui seu próprio método fazer_som(),
que é chamado de acordo com o tipo do objeto. Isso também é um exemplo de polimorfismo, pois objetos diferentes
têm comportamento diferente, mas são tratados de forma uniforme através da classe base Animal.
# Herança:
A herança é um conceito em POO que permite que uma classe herde atributos e métodos de outra classe. A classe herdada é chamada de classe derivada, enquanto a classe herdada é chamada de classe base.
Quando uma classe herda de outra, ela recebe automaticamente todos os atributos e métodos da classe base, podendo usá-los diretamente. Isso facilita a reutilização de código e estabelece uma relação de especialização, onde a classe derivada é uma versão mais específica da classe base.
### Exemplo:
Neste exemplo, a classe Carroherda da classe Veiculo. Isso significa que o carro tem acesso ao método acelerar()da classe Veiculosem precisar defini-lo novamente. Além disso, a classe Carrotambém pode ter seus próprios métodos, como o método abrir_porta().
```python
class Veiculo:
    def acelerar(self):
        print("O veículo está acelerando.")

class Carro(Veiculo):
    def abrir_porta(self):
        print("A porta do carro está aberta.")
```
Podemos criar um objeto da classe Carroe acessar seus métodos:
```python
meu_carro = Carro()
meu_carro.acelerar()     # Saída: O veículo está acelerando.
meu_carro.abrir_porta()  # Saída: A porta do carro está aberta.
```
Assim, a herança permite que a classe derivada aproveite o código da classe base, evitando duplicação e adicionando funcionalidades específicas, se necessário.

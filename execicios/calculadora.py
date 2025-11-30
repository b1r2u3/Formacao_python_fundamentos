# O desafio consiste em implementar uma classe Calculadora 
# que utilize os princípios da Programação Orientada a Objetos (POO). 
# A classe deve conter um método para realizar a operação de soma entre 
# dois números inteiros, encapsulando assim a lógica matemática da adição.


class Calculadora:
    def __init__(self):
        pass

    def somar(self, a:int, b:int) -> int:
        return a + b


n1 = int(input("n1: "))
n2 = int(input("n2: "))

calc = Calculadora()
resultado = calc.somar(n1, n2)
print(resultado)       
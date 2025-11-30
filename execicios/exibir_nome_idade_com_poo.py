class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_nome(self, nome, idade):
        print(f"Nome: {self.nome}, idade: {self.idade}")    

nome = input("nome: ")
idade = int(input("idade: "))
            
p1 = Pessoa(nome, idade)

p1.mostrar_nome(nome, idade)
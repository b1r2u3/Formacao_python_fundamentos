PI =  3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de  PI: {PI:10.2f}")

nome = "Bruno"
idade = 35
profissao = "programador"
linguagem = "python"

dados = {"nome": "Bruno", "idade": 35}

print("Nome: %s idade: %s" % (nome, idade))
print("Nome: {} idade: {}".format(nome, idade))
print("Nome: {0} idade: {1}".format(nome, idade))
print("Nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} idade: {idade}".format(**dados))
print(f"Nome: {nome} idade: {idade}")
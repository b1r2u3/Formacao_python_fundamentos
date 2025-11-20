def exibir_mensagem():
    print("Ola mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")    

def exibir_mensagem_3(nome="antonio"):
    print(f"Seja em vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="bruno")
exibir_mensagem_3()
exibir_mensagem_3(nome="joao")        

def calcular_total(numeros):
    return  sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero  + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 30]))
print(retorna_antecessor_e_sucessor(10))
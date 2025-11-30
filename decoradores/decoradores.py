def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a funcao.")
        funcao()
        print("Faz algo depois de executar a funcao.\n")

    return envelope

def ola_mundo():
    print("ola mundo!") 

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()       

# USANDO DECORADOR (AÇUCAR SINTATICO)
@meu_decorador
def ola_mundo1():
    print("ola mundo , usando o açucar sintatico")

ola_mundo1()
     
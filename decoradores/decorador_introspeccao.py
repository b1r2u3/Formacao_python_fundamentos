import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a funcao.")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar a funcao.\n")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"ola mundo {nome}!") 
    return nome.upper()

print(ola_mundo.__name__)   
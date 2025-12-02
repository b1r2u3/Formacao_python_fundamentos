def meu_decorador(funcao):
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

resultado = ola_mundo("Bruno")
print(resultado)   
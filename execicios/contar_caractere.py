def contar_caractere(string):
    contador = {}

    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1     
    return contador        

entrada = input()

resultado = contar_caractere(entrada)

print(resultado)
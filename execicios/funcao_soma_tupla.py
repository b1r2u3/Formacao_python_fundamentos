def soma_tupla(tupla):
    return sum(tupla)

# Leitura da entrada
entrada = input().split()

# Conversão para inteiros usando map(int, ...)
elementos = tuple(map(int, entrada))

# Cálculo da soma
resultado = soma_tupla(elementos)

# Saída final
print(f"A soma dos elementos da tupla é: {resultado}")

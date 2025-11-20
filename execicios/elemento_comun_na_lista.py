def elementos_comuns(lista1, lista2):
    try:
        lista1 = list(map(int, lista1.split()))
        lista2 = list(map(int, lista2.split()))
    except ValueError:
        if not all(item.lstrip('-').isdigit() for item in lista1):
            return print("Entrada inválida.")
        if not all(item.lstrip('-').isdigit() for item in lista2):
            return print("Entrada inválida.")    
    
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    comuns = conjunto1.intersection(conjunto2)
    comuns = list(comuns)

    return print(f"Elementos comuns ás duas lista: {comuns}")

l1 = input()
l2 = input()

elementos_comuns(l1, l2)
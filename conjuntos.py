
# SET -> retira elementos duplicados
a = set("abacaxi")

print(a)

linguagens = {"python", "java", "python"}

print(linguagens)
# =====================================
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
print(numeros[2])
# ======================================
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"indice [{indice}]: {carro}")
#===========================================

conjuto_a = {1, 2}
conjuto_b = {3, 4}

conjuto_a.union(conjuto_b)

conjuto_x = {1, 2, 3}
conjuto_y = {2, 3, 4}

conjuto_x.intersection(conjuto_y)

conjuto_x.difference(conjuto_y)
conjuto_y.difference(conjuto_x)
conjuto_x.symmetric_difference(conjuto_y)

conjunto_w = {1, 2, 3}
conjunto_z = {4, 1, 2, 5, 6, 3}

conjunto_w.issubset(conjunto_z)
conjunto_z.issubset(conjunto_w)

conjunto_w.issuperset(conjunto_z)
conjunto_z.issuperset(conjunto_w)

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {6, 7, 8}
conjunto_3 = {1, 0}

conjunto_1.isdisjoint(conjunto_2)
conjunto_1.isdisjoint(conjunto_3)
# =======================================================
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)
# ===============================================
n = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(n)

n.discard(1)
n.discard(45)

print(n)

print(n.pop())
print(n.pop())
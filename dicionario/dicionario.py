pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)
pessoa1 = dict(nome="Bruno", idade=35)

# Adicionar uma chave em um dicionario que ja existe
pessoa["telefone"] = "3333-1234"

# acessar dados no dicionario
pessoa["nome"]
pessoa["idade"]
pessoa["telefone"]

# alterando dados no dicionario
pessoa["nome"] = "maria"
pessoa["idade"] = 18
pessoa["telefone"] = "9988-11781"

print(pessoa)
# ===============================================


# dicionario aninhado
contatos = {
    "guilerme@gmail.com": {"nome": "guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "chappie", "telefone": "3444-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"]

# iterar sobre um dicionario

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)    

#=====================================================================
# metodos da classe dict
nomes = {"nome": "bruno", "sobrenome": "rogerio" }

print(nomes)

copia = nomes.copy()
nomes["chave"]   #se a chave nao exitir gera erro

nomes.get("chave")
nomes.get("chave", {})
nomes.get("nome")
nomes.items()
nomes.keys()
# nomes.pop("nome", {})
# nomes.popitem(")
nomes.setdefault("idade", 35)
nomes.values()
def salvar_carro(modelo, marca, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("palio" ,"fiat", 1999, "ABC-1234") # precisa ser na mesma ordem
salvar_carro(marca="fiat", modelo="palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"modelo": "palio", "marca": "fiat", "ano": "1999", "placa": "ABC-1234"}) #forma de dicionario

def exibir_poema(data_exxtenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_exxtenso} \n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terca-feira, 11 de novembro de 2025", 
             "zen of python", 
             "Beautiful is better than ugly", 
             "isso faz parte do poema", 
             autor="Tim peters", 
             ano=1999
             )    
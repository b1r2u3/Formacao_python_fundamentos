arquivo = open(
    "C:/Users/kbm/Desktop/projetos-programacao/dio/formação_python_fundamentals/" \
    "manipulacaoDeArquivo/lorem.txt",  "r", encoding='utf-8'
)

print(arquivo.read()) #----------> LÊ O CONNTEÚDO DE UMA VEZ
# print(arquivo.readline()) #------> LÊ UMA LINHA  POPR VEZ
# print(arquivo.readlines()) # ----> CARREGA O CONTEÚDO EM UMA LISTA

#tip
# while len(linha := arquivo.readline()):
#     print(linha)
arquivo.close()
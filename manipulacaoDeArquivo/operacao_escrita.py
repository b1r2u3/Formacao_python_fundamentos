arquivo = open("C:/Users/kbm/Desktop/projetos-programacao/dio/"
"formação_python_fundamentals/manipulacaoDeArquivo/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo. ")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"]) #--------> lista
arquivo.close()
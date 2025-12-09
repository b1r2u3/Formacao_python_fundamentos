import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent  #=========Pega o caminho do arquivo

os.mkdir(ROOT_PATH / "novo-diretorio") #==========>Cria um diretório

arquivo = open(ROOT_PATH / "novo.txt",  "w") #=========>Cria um arquivo 
arquivo.close() #===========>Fecha o arquivo

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") #=========Renomea o arquivo

os.remove(ROOT_PATH / "alterado.txt") #==========Remove o arquivo

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt") #=========Move o arquivo

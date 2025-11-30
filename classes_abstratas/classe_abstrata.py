from abc import ABC, abstractmethod

# Quando usa abstractmethod é obrigado as instanciar o metodo nas classes filhas

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass  

    @property
    @abstractmethod   
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv..")
        print("TV ligada!")
    
    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")

    def marca(self):
        print("LG")    

class ControlArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o arcondicionado..")
        print("Ar ligado!")
    
    def desligar(self):
        print("Desligando o ar...")
        print("Ar desligado!")  

    def marca(self):
        print("Philco")           

controletv = ControleTV()
controletv.ligar()
controletv.desligar()
controletv.marca()

controleAr = ControlArCondicionado()
controleAr.ligar()
controleAr.desligar()
controleAr.marca()


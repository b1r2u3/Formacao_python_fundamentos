class Conta:
    def __init__(self, nro_conta, saldo=0):
        self._saldo = saldo  #variavel privada começa com um underline 
        self.nro_conta = nro_conta

    def depositar(self, valor):
        #... implementação de verificação
        self._saldo += valor    

    def sacar(self, valor):
        #... implementação de verificação
        self._saldo -= valor

    def mostrar_saldo(self):
        #... implementação de verificação
        return self._saldo        
    
conta01 = Conta("0001", 100)
print(conta01.mostrar_saldo())
conta01.depositar(100)
print(conta01.mostrar_saldo())
print(conta01.nro_conta)
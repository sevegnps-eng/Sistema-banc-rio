# Criação da Classe conta

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

# Método depositar
        
    def depositar(self, entrada):
        if entrada <= 0:
            print("Valor inválido para depósito!")

            return

        self.saldo += entrada
        print(f"Você depositou R${entrada:.2f} e seu saldo agora é de R${self.saldo:.2f}")

# Método sacar

    def sacar(self, saque):
        if saque > self.saldo:
            print("Você não tem saldo suficiente disponível para saque! ")
            return
        
        if saque <= 0:
            print("Valor inválido para saque! ")
            return
        
        self.saldo -= saque
        print(f"Você sacou R${saque:.2f} e seu saldo atual é de R${self.saldo:.2f}")

# Método transferir

    def transferir(self, transferencia, outra_conta):
        if transferencia > self.saldo:
            print("Você não tem saldo suficiente para realizar uma transferência! ")
            return
        
        if transferencia <= 0:
            print("Valor inválido para trasnferência! ")
            return
        
        self.saldo -= transferencia
        outra_conta.saldo += transferencia

        print(f"Você transferiu R${transferencia:.2f} para {outra_conta.titular} e seu saldo agora é de R${self.saldo}")
    


gabriel = Conta("Gabriel", 1000)
eduardo = Conta("Eduardo", 1000)

gabriel.depositar(100000)
gabriel.transferir(43789, eduardo)




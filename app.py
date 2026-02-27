# Import 
import string

# Banco de dados
usuarios = []

# Classe Usuário

class Usuario():
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

# Definir senha
   
    def criar_senha(self, senha):

        if len(senha) < 12:
            print ("Sua senha deve ter no mínimo 12 caracteres")
            return
    
        if not any(maiuscula.isupper() for maiuscula in senha):
                print("Sua senha deve conter no mínimo um caractere maiúsculo")
                return
        
        if not any(minuscula.islower() for minuscula in senha):
            print("Sua senha deve conter no mínimo um caractere minúsculo")
            return
        
        if not any(numero.isdigit() for numero in senha):
            print("Sua senha deve conter no mínimo um número")
            return
        
        if not any(not simbolo.isalnum() for simbolo in senha):
            print("Sua senha deve conter símbolos")
            return

        return senha

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
joao = Conta("João", 0)



gabriel.depositar(100000)
gabriel.transferir(43789, eduardo)
gabriel.transferir(14780, joao)

joao.transferir(2000, eduardo)
print(eduardo.saldo)
print(joao.saldo)

gabrieu = Usuario("sevegnps!gmail.com", "1231231")
gabrieu.criar_senha("26a09b2003F#")



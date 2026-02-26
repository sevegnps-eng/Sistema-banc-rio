# Classe Usuário

class Usuario():
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

# Definir email
    def definir_email(self, email):
            
            if email.startswith("@"):
                print("Seu email não pode começar com @")
                return
            
            if email.count("@") != 1:
                print("Seu email deve conter apenas um @ ")
                return
            
            if email.endswith("@"):
                print("Seu email não pode terminar com @")
                return
            
            if "." not in email:
                print("seu email precisa ter um .")
                return
            
            if " " in email:
                print("seu email não pode conter espaços ")
                return
            
            return email

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

gabriel = Usuario("@sevegnps@gmail.com", "12312as")
gabriel.definir_email("sevegnps@gmail.com")


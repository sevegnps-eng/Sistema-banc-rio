# Banco de dados

usuarios = []

# Classe Usuário

class Usuario():
    def __init__(self, email, senha):
        self.validar_email(email)
        self.validar_senha(senha)
        self.email = email
        self.senha = senha

# Validação email

    def validar_email(self, email):

        if "@" not in email or email.startswith("@") or email.endswith("@"):
            raise ValueError("Email inválido")

# Validação senha
   
    def validar_senha(self, senha):

        if len(senha) < 12:
            raise ValueError("Sua senha deve ter no mínimo 12 caracteres")
    
        elif not any(maiuscula.isupper() for maiuscula in senha):
            raise ValueError("Sua senha deve conter no mínimo um caractere maiúsculo")
        
        elif not any(minuscula.islower() for minuscula in senha):
            raise ValueError("Sua senha deve conter no mínimo um caractere minúsculo")
        
        elif not any(numero.isdigit() for numero in senha):
            raise ValueError("Sua senha deve conter no mínimo um número")
        
        elif not any(not simbolo.isalnum() for simbolo in senha):
            raise ValueError("Sua senha deve conter símbolos")
            
# Cadastro do usuário:


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

# Programa principal

gabriel = Usuario("sevegnps@gmail.com", "26a09b2003F#")
print(usuarios)


import bcrypt

usuarios = []

# Classe Usuário
class Usuario():
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
        self.validar_senha(senha)
        self.hash_senha = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

# Validar senha
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
        
# Classe Conta:
class Conta():
    def __init__(self, numero_conta, usuario):
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.historico = []

    def ver_saldo(self):
        print(f"Olá {self.usuario.nome}, seu saldo atual é de R${self.saldo:.2f}")
  
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para depósito")
        self.saldo += valor
        self.historico.append(f"Você depositou R${valor:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para saque")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.historico.append(f"Você sacou R${valor:.2f}")

    def transferir(self, valor, outra_conta):
        if valor <= 0:
            raise ValueError("Valor inválido para transferência ")
        if valor > self.saldo:
            raise ValueError("Você não tem saldo suficiente para transferir ")
        self.sacar(valor)
        outra_conta.depositar(valor)
        self.historico.append(f"Você transferiu R${valor:.2f} para {outra_conta.usuario.nome}")

    def listar_historico(self):
        for historico in self.historico:
            print (historico)

# Classe Conta Corrente
class Conta_corrente(Conta):
    def __init__(self, numero_conta, usuario, limite, taxa_manutencao):
        super.__init__(numero_conta, usuario)
        self.limite = limite
        self.taxa_manutencao = taxa_manutencao

    def sacar(self):
        
        

gabriel_usuario = Usuario("Gabriel Sevegnani", "053.680.100-28", "123asd7120B#")
gabriel_conta = Conta("537", gabriel_usuario)
juliana_usuario = Usuario("Juliana Braga", "123.412.123-23", "123127ufshU#")
juliana_conta = Conta("123", juliana_usuario)
juliana_conta.depositar(1000)
juliana_conta.sacar(100)
juliana_conta.transferir(200, gabriel_conta)



    




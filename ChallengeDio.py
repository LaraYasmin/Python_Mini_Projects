class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

class ContaBancaria:
    limite_saque = 3
    limite_valor_saque = 500
    numero_conta_sequencial = 1
    
    def __init__(self, usuario, saldo_inicial=0):
        self.usuario = usuario
        self.saldo = saldo_inicial
        self.numero_saques = 0
        self.extrato = []
        self.numero_conta = ContaBancaria.numero_conta_sequencial
        self.agencia = "0001"
        ContaBancaria.numero_conta_sequencial += 1
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            return f"R${valor:.2f} depositado. Saldo atual: R${self.saldo:.2f}"
        else:
            return "Operação inválida"
    
    def sacar(self, valor):
        if valor <= 0:
            return "Operação inválida"
        
        if self.numero_saques >= self.limite_saque:
            return "Limite de saques diários atingido"
        
        if valor > self.limite_valor_saque:
            return f"Valor máximo de saque: R${self.limite_valor_saque:.2f}"
        
        if valor > self.saldo:
            return "Saldo insuficiente"
        
        self.saldo -= valor
        self.numero_saques += 1
        self.extrato.append(f"Saque: -R${valor:.2f}")
        return f"R${valor:.2f} sacado. Saldo atual: R${self.saldo:.2f}"
    
    def gerar_extrato(self):
        extrato_str = "\n".join(self.extrato) if self.extrato else "Sem movimentação"
        return f"Extrato:\n{extrato_str}\nSaldo atual: R${self.saldo:.2f}"

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        
    def cadastrar_usuario(self, nome, data_nascimento, cpf, endereco):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return "Erro: CPF já cadastrado"
        novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        return "Usuário cadastrado com sucesso"
    
    def cadastrar_conta_bancaria(self, cpf, saldo_inicial=0):
        usuario = None
        for u in self.usuarios:
            if u.cpf == cpf:
                usuario = u
                break
        if usuario is None:
            return "Erro: Usuário não encontrado"
        nova_conta = ContaBancaria(usuario, saldo_inicial)
        usuario.contas.append(nova_conta)
        self.contas.append(nova_conta)
        return f"Conta bancária {nova_conta.numero_conta} criada com sucesso para {usuario.nome}"
    
    def filtrar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return "Usuário não encontrado"
    
    def listar_contas(self):
        if not self.contas:
            return "Nenhuma conta cadastrada"
        contas_str = "\n".join(
            f"Conta {conta.numero_conta}, Agência {conta.agencia}, de {conta.usuario.nome} (CPF: {conta.usuario.cpf}) - Saldo: R${conta.saldo:.2f}"
            for conta in self.contas
        )
        return contas_str

banco = Banco()
print(banco.cadastrar_usuario("João Silva", "01/01/1990", "12345678900", "Rua A, 123, Bairro B, Cidade C - SP"))
print(banco.cadastrar_usuario("Maria Santos", "02/02/1985", "09876543211", "Rua X, 456, Bairro Y, Cidade Z - RJ"))
print(banco.cadastrar_usuario("João Silva", "01/01/1990", "12345678900", "Rua A, 123, Bairro B, Cidade C - SP"))
print(banco.cadastrar_conta_bancaria("12345678900", 1000))
print(banco.cadastrar_conta_bancaria("09876543211", 500))
print(banco.cadastrar_conta_bancaria("12345678900", 200))

conta_joao1 = next(conta for conta in banco.contas if conta.usuario.cpf == "12345678900" and conta.numero_conta == 1)
print(conta_joao1.depositar(200))
print(conta_joao1.sacar(100))
print(conta_joao1.gerar_extrato())

conta_maria = next(conta for conta in banco.contas if conta.usuario.cpf == "09876543211")
print(conta_maria.depositar(300))
print(conta_maria.sacar(600))
print(conta_maria.sacar(100))
print(conta_maria.gerar_extrato())

print(banco.listar_contas())
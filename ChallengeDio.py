class Banco:
    limite_saque = 3
    limite_valor_saque = 500
    
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.numero_saques = 0
        self.extrato = []
        
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
        extrato_str = "\n".join(self.extrato)
        if not extrato_str:
            return f"Extrato:\nSem movimentação"
        return f"Extrato:\n{extrato_str}\nSaldo atual: R${self.saldo:.2f}"

banco = Banco(0)
print(banco.depositar(50))
print(banco.sacar(30))
print(banco.sacar(30))
print(banco.gerar_extrato())
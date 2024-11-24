def cria_conta(numero, titular, saldo, limite):
   conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
   return conta

def depositar(conta, valor):
   conta["saldo"] += valor

def saque(conta, valor):
   conta["saldo"] -= valor

def extrato(conta):
   print(f'Conta: {conta["numero"]}')
   print(f'Titular: {conta["titular"]}')
   print(f'Saldo: {conta["saldo"]}')
   print(f'Limite: {conta["limite"]}')
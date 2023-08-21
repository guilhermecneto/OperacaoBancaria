menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
"""
saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
saque = 0



while True:
  opcao = input(menu)
  if opcao == "d":
    print("Depósito")
    deposito = input(deposito)
    deposito = int(deposito)

  elif opcao == "s":
    if(LIMITE_SAQUES )
    print("Saque")
    saque = input(saque)
    saque = int(saque)
    saldo = int(saldo)
    while(saque > saldo):
      print("Operação inválida")
      saque = input(saque)
      saque = int(saque)
      LIMITE_SAQUES = LIMITE_SAQUES - 1
    
  elif opcao == "e":
    print("Extrato")
    print("Seu saldo é de: R$ ")
    print(saldo)

  elif opcao == "q":
    break
  else:
    print("Operação Inválida, tente novamente")

  
  saldo = saldo + deposito - saque
  deposito = 0
  saque = 0

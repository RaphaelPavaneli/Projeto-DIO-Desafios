menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[l] sair

"""

saldo = 0
sacar = 0
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3


print(menu)

while True:
    opcao = input("Digite a opção: ")
    
    if opcao == 'd':
        depositar = float(input())

        if depositar > 0:
            saldo += depositar
            print(f"Deposito de {depositar: .2f} feito com sucesso!")
            print(f"Novo saldo: {saldo: .2f}")
            extrato += f"Deposito: R$ {depositar: .2f} \n" 

    elif opcao == 's':
        print(saldo)
        sacar = float(input())

        if sacar < saldo and sacar < 500:
            if numero_de_saques < LIMITE_SAQUES:
                saldo -= sacar
                print(f"Saque de {sacar: .2f} feito com sucesso!")
                numero_de_saques += 1
                extrato += f"Saque: R$ {sacar: .2f} \n"
            else:
                print("ERRO: \nNúmeros de saque diários atingidos")
        
        else:
            print("saque inválido!")

    elif opcao == 'e':
        print("\n Extrato da conta \n")
        print(extrato)
        print(f"\nSaldo da conta: R$ {saldo: .2f}")

    elif opcao == 'q':
        break

    else:
        print("Opção inválida")


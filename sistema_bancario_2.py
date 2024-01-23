import textwrap

def menu ():
    menu = """
    [nu]\tcriar usuario
    [nc]\tcriar contas
    [lc]\tlistar contas

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [l]\tsair

    ->  
    """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
      
    if valor > 0:
        saldo += valor
        print(f"Deposito de {valor: .2f} feito com sucesso!")
        extrato += f"Deposito: R$ {valor: .2f} \n" 

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n Extrato da conta \n")
    print(extrato)
    print(f"\nSaldo da conta: R$ {saldo: .2f}")

def saque(*, saldo_antigo , valor_sacado, saque_diario, L,conta):
    saldo_atualizado = saldo_antigo
    if valor_sacado < saldo_antigo and valor_sacado <= 500:
        if saque_diario < L:
            saldo_atualizado = saldo_antigo - valor_sacado
            print(f"Saque de {valor_sacado: .2f} feito com sucesso!")
            saque_diario += 1
            conta += f"Saque de: R$ {valor_sacado: .2f} \n"
        else:
            print("ERRO: \nNúmeros de saque diários atingidos")

    else:
        print("saque inválido!")
        
    return saldo_atualizado,saque_diario,conta

def criar_cliente(usuarios):

    cpf = input("Digite seu CPF:")
    
    usuario = filtrar_cliente(cpf, usuarios)

    if usuario:
        print("Usuario já cadastrado")
        return
    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereco: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cliente criado com sucesso!")


def filtrar_cliente(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF:")

    usuario = filtrar_cliente(cpf, usuarios)
    
    if usuario:
        print("Contra criada com sucesso!")
        return {"agencia:": agencia, "numero_conta": numero_conta, "usuario": usuario}

#arrumar depois
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    valor = 0
    extrato_conta = ""
    numero_de_saques = 0
    usuarios = []
    lista_contas = []


    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor= float(input("Digite o valor do depósito: "))
            saldo, extrato_conta = deposito(saldo,valor,extrato_conta)
            print(f"Novo saldo: {saldo: .2f}")

        elif opcao == 's':
            valor = float(input())
            saldo,numero_de_saques,extrato_conta = saque(L=LIMITE_SAQUES, saque_diario=numero_de_saques,saldo_antigo=saldo, 
                                                valor_sacado=valor,conta=extrato_conta)

        elif opcao == 'e':
            exibir_extrato(saldo,extrato=extrato_conta)

        elif opcao == 'nu':
            criar_cliente(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(lista_contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if lista_contas:
                lista_contas.append(conta)
    
        elif opcao == 'lc':
            listar_contas(lista_contas)


        elif opcao == 'q':
            break

        else:
            print("Opção inválida")



main()

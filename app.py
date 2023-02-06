menu = '''
    Bem vindo ao Assistente Bancário Virtual - 24hrs
    Escolha umas das opções:
    [d] - DEPOSITAR.
    [s] - SACAR.
    [e] - EXTRATO.
    [sd] - SALDO.
    
    [q] - Sair. 
'''

saldo = 0
extrato = ''
limite = 900

while True:
    opcao = input(f'{menu}\n Digite sua opção: ')

    # OPÇÃO DE DEPOSITO.
    if opcao == 'd':
        try:
            valor_depositado = int(input('Digite o valor do Deposito: '))

            if valor_depositado > limite:
                valor_depositado -= valor_depositado
                print('Limite do deposito é R$900')

            else:
                saldo += valor_depositado
                extrato += f'Deposito: R${valor_depositado:.2f}\n'
                print(f'R${valor_depositado:.2f} Foi depositado com sucesso!')

        except ValueError as e:
            print('DIGITE ALGO VALIDO')

    # OPÇÃO DE SAQUE.
    elif opcao == 's':
        try:
            valor_saque = int(input('Digite o valor do saque: '))
            if valor_saque > saldo:
                print('SALDO INDISPONIVEL')
            else:
                saldo -= valor_saque
                extrato += f'Saque de: R${valor_saque:.2f}\n'
                print(f'Valor sacado R${valor_saque:.2f}')
        except ValueError as e:
            print('DIGITE ALGO VALIDO')

    # EXTRATO.
    elif opcao == 'e':
        if not extrato:
            print('EXTRATO INEXISTENTE')
        else:
            print('EXTRATO BANCÁRIO'.center(50, '#')
                + '\n'
                + f'{extrato}')
            
    # SALDO.
    elif opcao == 'sd':
        if not saldo:
            print('SALDO INEXISTENTE')
        else:
            print(F'SALDO: R${saldo:.2f}')
    
    # SAIR.
    elif opcao == 'q':
        break

    else:
        print('ESCOLHA UMA OPÇÃO VALIDA')

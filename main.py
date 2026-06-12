import time
from apresentacao import ui

menu = (
    (1, 'Receita'),
    (2, 'Despesa'),
    (3, 'Saldo'),
    (4, 'Extrato'),
    (0, 'Sair')
)


# Programa Principal
saldo = 0
movimentos = []
while True:
    ui.titulo('SISTEMA FINANCEIRO')
    ui.texto(f'{" " * 20} {"Nº":<5}{"OPÇÃO":<20}', 3)
    ui.texto('-'*60, 3)
    for i, o in menu:
        ui.texto(f'{" " * 20} {i:<5}{o:<20}', 3)
    ui.texto('-'*60, 3)
    escolha = int(input('\nEscolha uma das opções: '))
    time.sleep(1)
    if escolha == 1:
        rec = float(input('Digite o valor da Receita R$'))
        desc = str(input('Descrição (salário, presente, freelance): '))
        movimentos.append({"tipo": "Receita", "valor": rec, "desc": desc})
        print('-'*60)
        print('Analisando...')
        print('-'*60)
        time.sleep(1)
        print('-'*60)
        print(f'SALDO ANTERIOR R${saldo:.2f}')
        print('-'*60)
        time.sleep(1)
        saldo += rec
        print(f'Saldo ATUAL R${saldo:.2f}')
        print('-'*60)
    elif escolha == 2:
        des = float(input('Digite o valor da Despesa R$'))
        if des > saldo:
            print(f'Não é possível realizar essa movimentação. Revise seu saldo.'
                  f'Saldo Atual R${saldo:.2f}')
        else:
            desc = str(input('Descrição (alimentação, lazer, aluguel): '))
            movimentos.append({"tipo" : "Despesa", "valor": des, "desc": desc})
            print('-'*60)
            print('Analisando...')
            print('-'*60)
            time.sleep(1)
            print(f'SALDO ANTERIOR R${saldo:.2f} e foi debitado o valor de R${des:.2f}.')
            print('-'*60)
            time.sleep(1)
            saldo -= des
            print(f'Saldo atual R${saldo:.2f}')
        print('-'*60)
    elif escolha == 3:
        time.sleep(1)
        print('-'*60)
        print('Calculando o saldo atual...')
        print('-'*60)
        time.sleep(1)
        print(f'O saldo atual é de R${saldo:.2f}.')
        print('-'*60)
    elif escolha == 4:
        time.sleep(1)
        print('-'*60)
        print('Buscando todas movimentações da conta...')
        print('-'*60)
        time.sleep(1)
        ui.titulo('EXTRATO ATUALIZADO')
        if len(movimentos) == 0:
            print('Sem movimentações na conta!')
            print('-' * 60)
        else:
            print(f'{"Nº":<5}{"Tipo":<15}{"Valor (R$)":<15}{"Descrição"}')
            for i, c in enumerate(movimentos, start=1):
                print(f'{i:<5}{c["tipo"]:<15}R$ {c["valor"]:>10.2f}   {c["desc"]}')
                time.sleep(0.1)
            print('-'*60)
            print(f'Saldo atual R${saldo:.2f}')
            print('-' * 60)
    elif escolha == 0:
        print('-' * 60)
        print('Saindo do sistema...')
        print('-' * 60)
        time.sleep(1)
        break
    else:
        print('COMANDO INVÁLIDO! TENTE NOVAMENTE'.center(60))

time.sleep(1)
ui.titulo('OBRIGADO POR UTILIZAR NOSSO PROGRAMA!'
       '\n PROGRAMA ENCERRADO!')

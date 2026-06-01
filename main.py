from time import sleep
def titulo(msg):
    print('-'*60)
    print(msg.center(60))
    print('-'*60)


# Programa Principal
titulo('SISTEMA FINANCEIRO')
saldo = 0

while True:
    print('1 - Receita')
    print('2 - Despesa')
    print('3 - Saldo')
    print('0 - Sair')
    escolha = int(input('\nEscolha uma das opções: '))
    sleep(1)
    if escolha == 1:
        rec = float(input('Digite o valor da Receita R$'))
        print('Analisando...')
        sleep(1)
        print(f'O saldo anterior era de R${saldo:.2f} e foi adicionado R${rec:.2f}.')
        sleep(1)
        saldo += rec
        print(f'Saldo Atual R${saldo:.2f}')
        print('-'*60)
    elif escolha == 2:
        des = float(input('Digite o valor da Despesa R$'))
        print('Analisando...')
        sleep(1)
        print(f'O saldo atual era de R${saldo:.2f} e foi debitado o valor de R${des:.2f}.')
        sleep(1)
        saldo -= des
        print(f'Saldo atual R${saldo:.2f}')
        print('-'*60)
    elif escolha == 3:
        sleep(1)
        print('Calculando o saldo atual...')
        sleep(1)
        print(f'O saldo atual é de R${saldo:.2f}.')
        print('-'*60)
    elif escolha == 0:
        print('Saindo do sistema...')
        sleep(1)
        break
    else:
        print('COMANDO INVÁLIDO! TENTE NOVAMENTE'.center(60))

sleep(1)
titulo('OBRIGADO POR UTILIZAR NOSSO PROGRAMA!'
       '\n PROGRAMA ENCERRADO!')

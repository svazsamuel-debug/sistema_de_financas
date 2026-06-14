def adicionar_receita(saldo, movimentos):
    '''
    Função para adicionar uma receita, atualizando o saldo e o extrato.
    Parâmetros:
    - saldo: valor atual do saldo
    - movimentos: lista de movimentações
    Retorna: o novo saldo atualizado
    Função criada por Samuel Vaz
    '''

    receita = float(input('Digite o valor da Receita R$'))
    descricao = input('Descrição (salário, presente, freelance): ')

    movimentos.append({
        "tipo": "Receita",
        "valor": receita,
        "desc": descricao
    })

    saldo += receita

    return saldo



def adicionar_despesa(saldo, movimentos):
     '''
     Função para adicionar uma despesa, atualizando o saldo e o extrato.
     Parâmetros:
     - saldo: valor atual do saldo
     - movimentos: lista de movimentações
     Retorna: o novo saldo atualizado
     Função criada por Samuel Vaz
     '''

     despesa = float(input('Digite o valor da despesa: R$'))

     if despesa > saldo:
         print('Não foi possível realizar sua movimentação. Revise seu saldo!')
         return saldo
          
     descricao = str(input('Descrição (alimentação, lazer, aluguel): '))

     movimentos.append({
         "tipo": "Despesa",
         "valor": despesa,
         "desc" : descricao
     })

     saldo -= despesa

     return saldo


def mostrar_saldo(saldo):
    '''
    Função para mostrar o saldo atual.
    Parâmetros:
    - saldo: valor atual do saldo
    Retorna: None
    Função criada por Samuel Vaz
    '''

    from time import sleep
    from apresentacao import ui

    sleep(0.5)
    print('-'*60)
    print('Calculando o saldo atual...')
    print('-'*60)
    sleep(0.5)
    ui.texto(f'O saldo atual é de R${saldo:.2f}.', 5)
    print('-'*60)
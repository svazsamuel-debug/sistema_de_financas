def adicionar_receita(saldo, movimentos):
    receita = float(input('Digite o valor da Receita R$'))
    descricao = input('Descrição (salário, presente, freelance): ')

    movimentos.append({
        "tipo": "Receita",
        "valor": receita,
        "desc": descricao
    })

    saldo += receita

    return saldo
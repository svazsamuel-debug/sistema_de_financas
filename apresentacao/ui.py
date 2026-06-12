def titulo(msg):
    '''
    titulo(msg)
    Função para padronizar os títulos utilizados no decorrer do sistema
    param msg: frase a ser destacada
    retorna a mensagem formatada
    ==============================
          MENSAGEM DE EXEMPLO
    ==============================
    Função criada por Samuel Vaz com base em aulas do Prof Guanabara
    '''
    texto('='*60, 3)
    texto(msg.center(60), 3)
    texto('='*60, 3)

def texto(msg, cores = 0):
    '''
    texto(msg, cores = 0)
    Função para atribuir cores às respostas de modo mais direto
    param msg: frase a ser colorida
    param cores: cor a ser escolhida pelo usuário
    0 - Sem cor (Cor padrão do terminal)
    1 - Vermelho
    2 - Verde
    3 - Branco
    4 - Azul
    5 - Roxo
    Função criada por Samuel Vaz
    '''
    print(f'{cor[cores]} {msg.ljust(60)} {cor[0]}')

cor = ('\033[m',          # 0 - Sem cor
       '\033[1;30;41m',   # 1 - Vermelho
       '\033[1;30;42m',   # 2 - Verde
       '\033[7;3m',       # 3 - Branco
       '\033[1;30;44m',   # 4 - Azul
       '\033[1;30;45m',   # 5 - Roxo
       )    
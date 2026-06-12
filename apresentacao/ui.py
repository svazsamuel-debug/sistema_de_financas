def titulo(msg):
    '''
    
    '''
    texto('='*60, 3)
    texto(msg.center(60), 3)
    texto('='*60, 3)

def texto(msg, cores = 0):
    print(f'{cor[cores]} {msg.ljust(60)} {cor[0]}')

cor = ('\033[m',          # 0 - Sem cor
       '\033[1;30;41m',   # 1 - Vermelho
       '\033[1;30;42m',   # 2 - Verde
       '\033[7;3m',       # 3 - Branco
       '\033[1;30;44m',   # 4 - Azul
       '\033[1;30;45m',   # 5 - Roxo
       )    
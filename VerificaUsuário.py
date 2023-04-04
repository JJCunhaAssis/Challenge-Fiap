import threading


def validar_placa(placa):
    placa_numeros = placa[:3]
    placa_letras = placa[3:]


blocklist = ['CUS', 'GAY', 'CKH']


def timeout():
    print('\n\nOperação encerrada devido falta de interação. ')
    exit()


while True:
    tempo = threading.Timer(10.00, timeout)
    tempo.start()
    entrada = input('>> Digite o número da placa ou aperte X para cancelar procedimento: ')

    tempo.cancel()

    if entrada.strip() == '':
        print('Nenhum valor digitado. Encerrando operação...')
        exit()

    if entrada.strip().upper() == 'X':
        print('Operação cancelada pelo usuário.')
        exit()

    entrada_sem_traco = entrada.replace('-', '')

    if len(entrada_sem_traco) == 6:
        if entrada_sem_traco[:3] in blocklist:
            print('A placa não deve conter essa sequência de letras. Digite novamente.\n')
        else:
            print(f'Placa digitada: {entrada_sem_traco}')
            break
    else:
        print('Placa inválida. Digite novamente.\n')

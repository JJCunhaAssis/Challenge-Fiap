import threading


#Função que define o tempo de interação do usuario. Caso ele não interaja, o programa fechará automaticamente.
def timeout():
    print('\n\nOperação encerrada devido falta de interação. ')
    exit()


while True:
    print('-=' * 45)
    print('        Olá! Seja bem-vindo ao Assistente de Modal da Porto!            ')
    print('-=' * 45)
    print('Escolha uma das opções abaixo: ')

    print('1 - Problemas Elétricos')
    print('2 - Problemas Mecânicos ou com cargas')
    print('3 - Problemas com Combustível ou Pneu')
    print('4 - Acidentes')
    print('5 - Sair')

    while True:
        tempo = threading.Timer(10.00, timeout)
        tempo.start()
        escolha_usuario = input("Escolha sua opção: ")

        tempo.cancel()

        try:
            escolha_usuario = int(escolha_usuario)
            if escolha_usuario not in [1, 2, 3, 4, 5]:
                print("Opção inválida. Digite apenas números de 1 a 5.")
            else:
                break
        except ValueError:
            print("Opção inválida. Digite apenas números de 1 a 5.")

    if escolha_usuario == 5:
        print('Operação encerrada pelo usuário')

        break

    if escolha_usuario == 1:
        print('\nVocê acessou o menu: 1 - Problemas Elétricos\n')
        while True:
            print('Qual seria o problema?  ')
            print('1 - Bateria')
            print('2 - Alternador')
            print('3 - Ignição')
            print('4 - Voltar ao menu anterior')
            escolha_eletrico = input('Escolha sua opção: ')
            if escolha_eletrico == '4':
                break
            elif escolha_eletrico in ['1', '2', '3']:
               escolha_eletrico2 = input(('Seu veículo possui carga? [Digite S/N] '))
               if escolha_eletrico2 == 'S':
                   carga_eletrico = float(input('Qual seria o peso aproximadamente?  (Digite com pontos, por exemplo: 23.5)\n'))
               print('Informações recebidas!')
               exit();
            elif escolha_eletrico2 == 'N':
                print('Informações recebidas')
                exit();
    if escolha_usuario == 2:
        print('\nVocê acessou o menu 2: - Problemas Mecânicos ou com cargas\n')
        while True:
            print('Qual seria o problema?  ')
            print('1 - Motor')
            print('2 - Transmissão ou freios')
            print('3 - Suspensão ou eixos')
            print('4 - Direção')
            print('5 - Carga tombada')
            print('6 - Voltar ao menu anterior')
            escolha_mecanico = input('Escolha sua opção: ')
            if escolha_mecanico == '6':
                break
            elif escolha_mecanico in ['1', '2', '3', '4']:
                escolha_mecanico2 = input('Seu veículo possui carga? [Digite S/N] ')
                if escolha_mecanico2 == 'S':
                    carga_mecanico = float(input('Qual seria o peso aproximadamente?  (Digite com pontos, por exemplo: 23.5)\n'))
                print('Informações recebidas!')
                exit();
            elif escolha_mecanico2 == 'N':
                print('Informações recebidas')
                exit();
    if escolha_usuario == 3:
        print('\nVocê acessou o menu: 3 - Problemas com Combustível ou Pneu\n')
        while True:
            print('Qual seria o problema?  ')
            print('1 - Falta de Combustível')
            print('2 - Combustível adulterado')
            print('3 - Pneu furado')
            print('4 - Voltar ao menu anterior')
            escolha_comb = input('Escolha sua opção: ')
            if escolha_comb == '4':
                break
            elif escolha_comb in ['1', '2', '3']:
                escolha_comb2 = input('Seu veículo possui carga? [Digite S/N] ')
                if escolha_comb2 == 'S':
                    carga_comb = float(input('Qual seria o peso aproximadamente?  (Digite com pontos, por exemplo: 23.5)\n'))
                print('Informações recebidas!')
                exit();
            elif escolha_comb2 == 'N':
                print('Informações recebidas!')
                exit();
    if escolha_usuario == 4:
        print('\nVocê acessou o menu: 4 - Acidentes\n')
        while True:
            print('Qual seria o problema? ')
            print('1 - Capotamento')
            print('2 - Batida frontal')
            print('3 - Veículo atingido')
            print('4 - Voltar ao menu anterior')
            escolha_acidente = input('Escolha sua opção: ')
            if escolha_acidente == '4':
                break
            elif escolha_acidente in ['1', '2', '3']:
                escolha_acidente2 = input('Seu veículo possui carga? [Digite S/N] ')
                if escolha_acidente2 == 'S':
                    carga_acidente = float(input('Qual seria o peso aproximadamente?  (Digite com pontos, por exemplo: 25.3)\n'))
                print('Informações recebidas!')
                exit();
            elif escolha_acidente2 == 'N':
                print('Informações recebidas!')
                exit();


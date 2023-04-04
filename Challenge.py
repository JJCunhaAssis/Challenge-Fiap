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
        escolha_usuario = input("Escolha sua opção: ")
        try:
            escolha_usuario = int(escolha_usuario)
            if escolha_usuario not in [1, 2, 3, 4, 5]:
                print("Opção inválida. Digite apenas números de 1 a 5.")
            else:
                break
        except ValueError:
            print("Opção inválida. Digite apenas números de 1 a 5.")

    if escolha_usuario == 5:
        break

    if escolha_usuario == 1:
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
               escolha_eletrico2 = input(('Seu veículo possui carga? [S/N] '))
               if escolha_eletrico2 == 'S':
                   carga_eletrico = float(input('Qual seria o peso aproximadamente?  (Digite com pontos, por exemplo: 23.5)\n'))










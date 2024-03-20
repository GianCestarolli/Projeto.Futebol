import os


def opcao_invalida():
    os.system ('cls')
    input('Opção inválida!\nDigite qualquer coisa para voltar ao menu:')
    menu()
    

def nome_do_programa():
    print('\n𝐒𝐨𝐜𝐜𝐞𝐫 𝐒𝐭𝐚𝐭𝐬\n')

def exibir_ligas():
    print('1. Premier League\n'
      '2. Serie A\n'
      '3. La liga\n'
      '4. Brasileirão\n')

def escolher_ligas(): 
    try:
        escolha = int(input('Bem vindo ao Soccer Stats!\nDigite o número da liga que gostaria de analisar:'))
        if escolha == 1:
            os.system ('cls')
            print('Premier League')
        elif escolha == 2:
            os.system ('cls')
            print('Serie A')
        elif escolha == 3:
            os.system ('cls')
            print('La liga')
        elif escolha == 4:
            os.system ('cls')
            print('Brasileirão')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def menu():
    os.system ('cls')
    nome_do_programa()
    exibir_ligas()
    escolher_ligas()

menu()







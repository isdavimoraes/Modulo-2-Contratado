###########################
#    Davi de Moraes       # 
#    Projeto Individual 2 #
###########################

      
#importe para colcoar sleep
from os import system, name
from time import *
#def para limpar a tela
def limpaTela():
    if name == 'nt':
        X = system('cls')  # SISTEMA WINDOWS
    else:
        X = system('clear')  # SISTEMA LINUX
    return X 
#Váriaveis de lista para guardar as infos

Cand_vag1 = {}
Cand_vag2 = {}
Cand_apro1 = {}
Cand_apro2 = {}
#Função para salvar as informações que o usuario fornece para sarlvar nas listas
def cadastro():
    sair = ' '  #menu de sair
    menu = ' '  #menu para selecionar em qual vaga o usuario irá se encaixar.
    while sair:
        nomes = input('Digite o nome do Candidato:\n')
        curriculo = input('Digite suas qualificações:\n').lower()      
        menu = input('Em qual vaga você gostaria de adicionar o candidato? \n [1] Vaga 1 \n [2] Vaga 2\n')
      

        if menu == '1':
            Cand_vag1.update({nomes:curriculo})
            if 'python' and 'programação' and 'desenvolvimento' in curriculo:
                Cand_apro1.update({nomes:curriculo})
            for k, v in Cand_vag1.items():
                print(f'{k} foi adicionado na VAGA1 com as expecificações:\n {v}.')


        elif menu == '2':
            Cand_vag2.update({nomes:curriculo})
            if 'analise de dados' and 'dados' and 'sql' in curriculo:
                Cand_apro2.update({nomes:curriculo})            
            for k, v in Cand_vag2.items():
                print(f'{k} foi adicionado nos dados da Vaga 2  com as expecificações:\n {v}.')
        #Aqui pergunta ao usuario se quer sair ou continuar
        sair = input('Deseja incluir mais alguém?\n [1] Sim \n [0] Não\n')
        if sair == '0':
            print('Todas as informações foram salvas no banco de dados.\n Em 7 segudo você terá a quantidade de candidados aplicados para a vaga e os aptos\n') 
            sleep(7) #sleep de 7s para limpar a tela
            limpaTela() #limpa a tela para uma melhor organização  
            break
        else:
            pass


cadastro() #Chamando a função def que é responsável em filtrar e salvar os candidatos em suas determinadas vagas.


def resultado():
    print(f' O número de candidatos aplicados para vaga 1 é de {len(Cand_vag1)} pessoas.\n')
    print(f' O número de candidatos que estão aptos a vaga 1 é de {len(Cand_apro1)} pessoas.\n')
    print(f' O número de candidatos aplicados para vaga 2 é de {len(Cand_vag2)} pessoas.\n')
    print(f' O número de candidatos que estão aptos a vaga 2 é de {len(Cand_apro2)} pessoas.\n')


resultado() #chama a função def que é responsável em dar o resultado




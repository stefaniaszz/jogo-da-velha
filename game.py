""" 
Jogo da Velha
"""
#inicia o tabuleiro pronto para jogar
def mostrar_tabuleiro(tab):
    for linha in tab:
        print(' | '.join(linha)) #junta as linhas e mostra o '|' no meio 

#verifica o vencedor
def verificar_vitoria(tab, jogador):
    for i in  range(3): #verifica 3 linhas, colunas ou diagonal como mesmo símbolo para indicar o vencedor
        #verificador de linhas
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True #se tiver tudo igual, o jogador ganhou
        
         
         #verificador de colunas
    for i in  range(3):
        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True #se tiver tudo igual, o jogador ganhou
        
           #verificador de diagonais
        if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
            return True #se tiver tudo igual, o jogador ganhou
        if tab [0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
            return True

    return False #senão, indica que não ganhou

#linhas e colunas do tabuleiro
tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']] 
jogador_atual = 'X'

#nove rodadas para finalizar o programa
for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f'Jogador {jogador_atual}, escolha uma posição (1-9):')
    #converte a escolha da posição em int e o (-1) anula aquela casa para que o próximo jogador não escolha a mesma
    pos = int(escolha) - 1
    #faz a lógica para encontrar a casa selecionada dentro da lista, usando as linhas e colunas
    linha, coluna = pos // 3, pos % 3 
    #verifica se a posição escolhida está ocupada
    if tabuleiro[linha][coluna] in ['X', 'O']: 
        print('Posição já ocupada. Tente outra.')
        continue
    #troca o jogador toda vez que finalizar esse loop for
    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f'Jogador {jogador_atual} venceu!')
        break

    #se o jogador atual for O, ele troca para X
    if jogador_atual == 'O':
        jogador_atual ='X'
    #se o jogador atual for X, ele troca para O
    else:
        jogador_atual = 'O'

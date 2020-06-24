
from sys import exit

#Lista declarada GLOBALMENTE
lista = ('NORTE', 'LESTE', 'SUL', 'OESTE')
#[Norte, Leste, Sul, Oeste] - Sentido horário


def direciona(comando, n):
    if comando == 'l':
        # if/else de UMA linha cada um
        if n == -4: return n + 3
        else: return n - 1
    
    elif comando == 'r': return n + 1


def atualiza_direcao(posicao, n):
    # Se n for maior que 4, só importa 
    # o resto da divisão por 4 
    try:
        if n > 4:
            posicao[3] = lista[n % 4]
            return posicao
        else:
            posicao[3] = lista[n]
            return posicao
    except Exception as e:
        # Caso dê alguma exceção, ele para o programa
        print(f"\nERRO FATAL! {str(e)}\n\nProvável comando escrito errado!\n")
        exit(1)



def move(comando, posicao, n):
    #Atualiza a posição com base no índide n
    #Para poder averiquar aonde que moverá-se o submarino
    posicao = atualiza_direcao(posicao, n)

    if posicao[3] == 'NORTE':
        posicao[1] = posicao[1] + 1
    elif posicao[3] == 'LESTE':
        posicao[0] = posicao[0] + 1
    elif posicao[3] == 'SUL':
        posicao[1] = posicao[1] - 1
    elif posicao[3] == 'OESTE':
        posicao[0] = posicao[0] - 1
    else:
        pass
    return posicao


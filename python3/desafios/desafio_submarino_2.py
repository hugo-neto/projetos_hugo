#!/usr/local/bin/pytho3
# -*- coding: utf-8 -*-

# Link do desafio:
# https://github.com/buscape-company/exercicios/tree/master/java


from sys import exit
from cima_baixo_str import limpa_input, tira_z, soma_z
from foca import direciona, atualiza_direcao, move
from salva_dados import salva_valores


# Lista declarada GLOBALMENTE
lista = ('NORTE', 'LESTE', 'SUL', 'OESTE')
# [Norte, Leste, Sul, Oeste] - Sentido horário


def muda_posicao(comando, posicao, n):
    try:
        # Simula um sitch(){} em python3
        dicionario = {
            'u': soma_z,
            'd': tira_z,
            'm': move,
        }
        # Gera uma função chamável acessável pelo next()
        # CHAMA: funcao(*parametros)

        movimento = next(
            valor for chave, valor in dicionario.items() if comando in chave)
        return movimento(comando, posicao, n)

    except Exception as e:
        # Tratamento de erro, caso algum comando esteja errado
        print(f"ERRO! {str(e)}")
        print("O programa não pode finalizar a movimentação do submarino.\n\tERRO FATAL!")
        exit(1)


def main():
    # Recebe os dados do usuários
    usuario = input("\tDigite os comandos a serem seguidos:\n\t")

    # Transforma a string em um texto único e sem (.) ou (,)
    usuario, n = limpa_input(usuario), 0

    posicao = [0, 0, 0, lista[n]]
    inicio = tuple(posicao)
    # Inicia um posicional (0,0,0,n)
    #                   (x,y,z,DIREÇÃO)

    # Acessa letra por letra
    for letra in usuario:
        if letra == 'l' or letra == 'r':
            # Se for 'l' ou 'r' é como se o submarino mudasse a sua direção
            # (ou apontasse para outra direção) mas não saísse do lugar
            n = direciona(letra, n)

        else:
            posicao = muda_posicao(letra, posicao, n)
            # Essa função faz ele mover-se em x, y, z

    # Deixa a posição atualizada para o print abaixo
    posicao = atualiza_direcao(posicao, n)
    opcao_salvar = input(
        "Aperte s para salvar, ou qualquer outra tecla para desconsiderar os dados:")

    # Exibe ao usuário nova situação so submarino
    print(f"{posicao[0]} {posicao[1]} {posicao[2]} {posicao[3]}")

    # Decide se o usuário quer ou não salvar
    if opcao_salvar == 's' or opcao_salvar == 'S':
        print("Salvando os dados")
        salva_valores(posicao, inicio)
        print("Programa salvo com sucesso!")

    print("Progra executado corretamente!")


if __name__ == '__main__':
    main()

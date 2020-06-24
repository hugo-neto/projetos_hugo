from sys import exit

def limpa_input(lista):
    #Agrupa e tira qualquer caracter residual e transforma em uma string única
    return lista.replace(" ","").replace(".","").replace(",","").lower()


def erro_funcao(comando):
    print("Erro ao executar o programa!")
    print(f"Código '{comando}' digitado errado!")
    print("Encerrando código, erro fatal!")
    exit(1)


def tira_z(comando, posicao, n):
    if comando == 'd':
        posicao[2] = posicao[2] - 1
        return posicao
    else:
        erro_funcao(comando)

def soma_z(comando, posicao, n):
    if comando == 'u':
        posicao[2] = posicao[2] + 1
        return posicao
    else:
        erro_funcao(comando)

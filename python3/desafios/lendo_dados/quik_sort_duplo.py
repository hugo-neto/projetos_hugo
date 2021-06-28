
# Defina as listas x e y como global
# CHAMAR: ordena_lista(x, y, 0, len(x)-1, i)


def ordena_lista(x, y, inicio, fim):
    direita = fim
    esquerda = inicio
    meio = int((direita + esquerda)/2)
    pivo = x[meio]
    
    while direita > esquerda:
        
        while x[esquerda] < pivo:
            esquerda = esquerda + 1
        
        while x[direita] > pivo:
            direita = direita - 1
        
        if esquerda <= direita:
            aux1 = x[esquerda]
            aux2 = y[esquerda]
            x[esquerda] = x[direita]
            y[esquerda] = y[direita]
            x[direita] = aux1
            y[direita] = aux2
            esquerda = esquerda + 1
            direita = direita - 1

        if inicio < direita:
            ordena_lista(x, y, inicio, direita)
        elif esquerda < fim:
            ordena_lista(x, y, esquerda, fim)
        else:
            pass


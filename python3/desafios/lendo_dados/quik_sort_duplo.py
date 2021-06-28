
# Defina as listas x e y como global
# CHAMAR: ordena_lista(x, y, 0, len(x)-1, i)


def ordena_lista(x, y, inicio, fim, i):
    direita = fim
    esquerda = inicio
    meio = int((direita + esquerda)/2)
    pivo = float(x[meio])
    
    while direita > esquerda:
        
        A = float(x[esquerda])
        while A < pivo:
            esquerda = esquerda + 1
            A = float(x[esquerda])
        
        A_ = float(x[direita])
        while A_ > pivo:
            direita = direita - 1
            A_ = float(x[direita])
        
        if esquerda <= direita:
            i = i + 1
            aux1 = x[esquerda]
            aux2 = y[esquerda]
            x[esquerda] = x[direita]
            y[esquerda] = y[direita]
            x[direita] = aux1
            y[direita] = aux2
            esquerda = esquerda + 1
            direita = direita - 1

        if inicio < direita:
            ordena_lista(x, y, inicio, direita, i)
        elif esquerda < fim:
            ordena_lista(x, y, esquerda, fim, i)
        else:
            pass


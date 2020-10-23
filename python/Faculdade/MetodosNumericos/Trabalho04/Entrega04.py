# ATENÇÃO: LEIA DE BAIXO PARA CIMA


# Gera a matriz P usada para determinar a posição do b
# Está como sendo primeiro porque ela é necessário para que P seja global
def gera_matriz_P(N):
    P = []
    for i in range(0, N):
        P.append(i+1)
    return P


# O valor de N fica salvo globalmente
N = int(input("Digite o valor de N da matriz quadrada NxN: "))
# Variável Global
P = gera_matriz_P(N)


# Gera matriz NxN com zero em todos a[i][j]
def gera_matriz(N):
    a = []
    for i in range(0,N):
        a.append( [0] * N ) 
    return a


def adiciona_valores_matriz(N):
    # Gera a matriz quadrada NxN e um vetor
    # de pivotamento: [1, 2, 3, ... , N]
    a = gera_matriz(N)
    # Adiciona valores na matriz 'Zerada'
    for i in range(0,N):
        for j in range(0,N):
            a[i][j] = float(input(f"Digite o termo a{i+1}{j+1}: "))
    return a


def gera_vetor_b(N):
    b = []
    print("Digite os valores do vetor b abaixo:")    
    for i in range(0, N):
        valor = float(input(f"Digite o valor do termo b[{i+1}]: "))
        b.append(valor)
    return b


# Função para printar matriz
def printa_matriz(a, N):
    for i in range(0, N):
        print("")
        for j in range(0, N):
            print('%+4.5f' % a[i][j], end=" ")
    print("")
    print("")


def pivota_matriz(a, N, i):
    global P
    comparativo = abs(a[i][i])
    for j in range(i, N):
        if abs(a[j][i]) > comparativo:
            comparativo = abs(a[j][i])
            aux1 = a[j]
            a[j] = a[i]
            a[i] = aux1
            
            aux2 = P[j]
            P[j] = P[i]
            P[i] = aux2
    return a


def extrai_L(a, N):
    L = gera_matriz(N)
    for i in range(0,N):
        L[i][i] = 1
        for j in range(0,i):
            L[i][j] = a[i][j]
    return L


def extrai_U(a, N):
    U = gera_matriz(N)
    for i in range(0,N):
        for j in range(i,N):
            U[i][j] = a[i][j]
    return U


def troca_b(b, N):
    global P
    bf = [0] * N
    for i in range(0, N):
        bf[i] = b[P[i]-1]
    P = [1,2,3,4]
    return bf


def subs_direta(a, b, N):
    y = [0] * N
    y[0] = b[0]
    for i in range(1, N):
        y[i] = b[i]
        for j in range(0, i):
            y[i] = y[i] - a[i][j]*y[j]
    return y


def retro_subs(a, y, N):
    x, n = [0] * N, N-1
    x[n] = y[n]/a[n][n]
    for i in range(n-1, -1, -1):
        x[i] = (1/a[i][i])*(y[i])
        for j in range(i+1, N):
            x[i] = x[i] - (1/a[i][i])*(a[i][j]*x[j])   
    return x


def printa_vetor_unit(vetor, N):
    for i in range(0, N):
        print("x" + str(i+1) + ". " + "{:.4f}".format(vetor[i]))


def Doolittle(a, N):
    for k in range(0, N-1):
        a = pivota_matriz(a, N, k)
        for i in range(k+1, N):
            a[i][k] = a[i][k]/a[k][k]
        for i in range(k+1, N):
            for j in range(k+1, N):
                a[i][j] = a[i][j] - a[i][k]*a[k][j]    
    return a


def printa_tudo(a, L, U, x, N):
    print("")
    print("Abaixo, a matriz A: ", end="")
    printa_matriz(a, N)

    print("Abaixo, a matriz L: ", end="")
    printa_matriz(L, N)
    
    print("Abaixo, a matriz U: ", end="")
    printa_matriz(U, N)
    
    print("Abaixo, o vetor solução: ")
    printa_vetor_unit(x, N)
    print("")


def main():
    a = adiciona_valores_matriz(N)
    b = gera_vetor_b(N)
    a = Doolittle(a, N)

    L = extrai_L(a, N)
    U = extrai_U(a, N)

    b = troca_b(b, N)
    y = subs_direta(L, b, N)
    print(f"Vetores: \n1. P = {P}\n2. b = {b}\n3. y = {y}")
    
    x = retro_subs(a, y, N)
    
    printa_tudo(a, L, U, x, N)
    

if __name__=='__main__':
    main()

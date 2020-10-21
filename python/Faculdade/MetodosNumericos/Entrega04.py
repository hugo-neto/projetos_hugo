

# Gera a matriz P usada para determinar
# a posição do b
# Está como sendo primeiro porque ela é 
# necessário para que P seja global
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


def adiciona_valores_matriz(a, N):
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

# PROBLEMA! 
def pivota_matriz(a, N, i):
    global P
    comparativo = abs(a[i][i])
    for j in range(i, N):
        if abs(a[j][i]) > comparativo:
            comparativo = a[j][i]
            aux = a[j]
            a[j] = a[i]
            a[i] = aux
            
            aux = P[i]
            P[i] = P[j]
            P[j] = aux
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
    for i in range(0, N):
        if (P[i] - 1) != i:
            p_indice = (P[i] - 1)
            valor_b_depois = b[p_indice]
            valor_b_antes  = b[i]
            b[i] = valor_b_depois
            b[p_indice] = valor_b_antes
            P[i] = i+1
            P[p_indice] = p_indice + 1
    return b


def subs_direta(a, b, N):
    y = [0]*N
    y[0] = (b[0])
    for i in range(1,N):
        aux = b[i]
        for j in range(0, N):
            aux = aux - a[i][j]*y[j]
        y[i] = aux
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


def printa_tudo(L, U, x, N):
    print("")
    print("Abaixo, a matriz L: ", end="")
    printa_matriz(L, N)
    
    print("Abaixo, a matriz U: ", end="")
    printa_matriz(U, N)
    
    print("Abaixo, o vetor solução: ")
    printa_vetor_unit(x, N)
    print("")


def main():
    # Gera a matriz quadrada NxN e um vetor
    # de pivotamento: [1, 2, 3, ... , N]
    a = gera_matriz(N)
    # Adiciona valores na matriz 'Zerada'
    a = adiciona_valores_matriz(a, N)
    b = gera_vetor_b(N)
    
    a = Doolittle(a, N)
    
    L = extrai_L(a, N)
    U = extrai_U(a, N)
    
    b = troca_b(b, N)

    # Parece estranho, mas o vetor y não é salvo. Ele
    # só retorna o valor necessário para retro_subs()    
    x = retro_subs(a, subs_direta(a, b, N), N)
    
    printa_tudo(L, U, x, N)


if __name__=='__main__':
    main()

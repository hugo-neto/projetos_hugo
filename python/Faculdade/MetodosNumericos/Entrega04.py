

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


def printa(a, N):
    for i in range(0, N):
        print("")
        for j in range(0, N):
            print('%+4.5f' % a[i][j], end=" ")
    print("")


def pivota_matriz(a, N):
    pass


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


def Doolittle(a, N):
    for k in range(0, N-1):
        # a = pivota_matriz(a, N)
        for i in range(k+1, N):
            a[i][k] = a[i][k]/a[k][k]
        for i in range(k+1, N):
            for j in range(k+1, N):
                a[i][j] = a[i][j] - a[i][k]*a[k][j]    
    return a


def main():
    aux, N = 0, 3
    a = gera_matriz(N)
    a = adiciona_valores_matriz(a, N)
    a = Doolittle(a, N)
    L = extrai_L(a, N)
    U = extrai_U(a, N)
    printa(U, N)


if __name__=='__main__':
    main()



def gera_matriz(N):
    a = []
    for i in range(0,N):
        a.append( [0] * N ) 
    return a


def altera_matriz(a, N):
    for i in range(0,N):
        for j in range(0,N):
            a[i][j] = float(input(f"Digite o termo a{i+1}{j+1}: "))
    return a


def printa(a, N):
    for i in range(0, N):
        print("")
        for j in range(0, N):
            print('%+4.4f' % a[i][j], end=" ")
    print("")

def Doolittle(a, N):
    for k in range(0, N-1):
        for i in range(k+1, N):
            for j in range(k+1, N):
                a[i][k] = a[i][k]/a[k][k]
                a[i][j] = a[i][j] - a[i][k]*a[k][j]
    return a


def main():
    aux, N = 0, 3
    a = gera_matriz(N)
    a = altera_matriz(a, N)
    a = Doolittle(a, N)
    printa(a, N)


if __name__=='__main__':
    main()

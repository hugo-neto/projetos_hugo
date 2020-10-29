from math import sinh


def f(x):
    c = 251/200
    return 3*x*sinh(c*x)/sinh(c)


def inicial(a, b, N, criterio_convergencia, epslon):
    S0 = f(a) - f(b)
    h = (b-a)/(2*N)
    Simpar, Spar = 0, 0
    for j in range(1,N+1):
        dentro = a + (2*j-1)*h        
        Simpar = Simpar + f(dentro)
    if N > 1:
        for j in range(1,N):
            dentro = a + 2*j*h        
            Spar = Spar + f(dentro)
    else:
        Spar = 0
    I = (h/3)*(S0 + 4*Simpar + 2*Spar)
    Ivelho = 0
    
    while (abs(I - Ivelho) > criterio_convergencia) and (abs(h) > epslon):
        Ivelho = I
        N = N + N
        h = h/2
        Spar = Spar + Simpar
        Simpar = 0
        for j in range(1,N+1):
            dentro = a + (2*j-1)*h
            Simpar = Simpar + f(dentro)
        I = (h/3)*(S0 + 4*Simpar + 2*Spar)
    
    I = (16*I - Ivelho)/15
    print(f"Para o intervalo [{a}, {b}] teremos o valor de integral {I}")
    print(f"Critério utilizado foi Delta = {criterio_convergencia} e Epslon = {epslon}")
    print(f"O Número de intervalos (N) = {N}")    
    return I
    


def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    N = float(input("Digite o valor de N: "))
    while N <= 0:
        N = float(input("Digite um valor de N maior que 0: "))
    criterio_convergencia = float(input("Digite o valor do critério de convergência: "))
    epslon = float(input("Digite o valor de epslon (Menor valor do passo de integração): "))
    I = inicial(a, b, N, criterio_convergencia, epslon)
    printa(a, b, I, criterio_convergencia, epslon)    


if __name__=='__main__':
    main()

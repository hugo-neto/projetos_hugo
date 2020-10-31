# Aluno: Hugo de Lacerda Coutinho Neto
# DRE: 118060251

from sympy import Integral, symbols, sinh
import math


def f(x):
    c = 251/200
    return 3*x*math.sinh(c*x)/math.sinh(c)


def Ireal(a, b):
    # Is = I sympy
    x = symbols('x')
    c = 251/200
    valor = Integral((3*x*sinh(c*x)/sinh(c)),(x,a,b)).doit()
    return valor


def Simpson(a, b, N, criterio_convergencia, epslon):
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
    
    
    I1 = I
    # Is = I sympy
    Is = Ireal(a, b)
    I = (16*I - Ivelho)/15
    
    I2 = I
    
    print(f"\nPara o intervalo [{a}, {b}] teremos o valor de integral {I}")
    print(f"Critério utilizado foi Delta = {criterio_convergencia} e Epslon = {epslon}")
    print(f"O Número de intervalos (N) = {N} e o Valor = {h}\n")
    print(f"Montante da correção de Richardson em valor absoluto: {abs(I2-I1)}")
    print(f"Ivelho = {I1} I = {I2}")    
    print(f"Antes da extrapolação de Richardson |Ie - I| = {abs(Is - I1)}")
    print(f"Depois da extrapolação de Richardson |Ie - I| = {abs(Is - I2)}\n")
    
    return I
    


def main():
    condicao = False
    
    while condicao == False:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        N = int(input("Digite o valor de N: "))
        
        while N <= 0:
            N = float(input("Digite um valor de N maior que 0: "))
        
        criterio_convergencia = float(input("Digite o VALOR do critério de convergência sabendo que 10**-VALOR: "))
        criterio_convergencia = 10**-abs(criterio_convergencia)
        
        epslon = float(input("Digite o VALOR de epslon (Menor valor do passo de integração) sabendo que 10**-VALOR: "))
        epslon = 10**-abs(epslon)
        
        I = Simpson(a, b, N, criterio_convergencia, epslon)
        
        usuario = input("Digite a tecla 's' para reiniciar o programa ou qualquer outra para terminá-lo: ")
    
        if usuario == 's':
            pass
        else:
            condicao = True
    
    print("\nObrigado\n")


if __name__=='__main__':
    main()

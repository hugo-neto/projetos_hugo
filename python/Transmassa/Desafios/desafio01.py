

import pandas as pd
from math import pi, exp, sin


def razao_sem(Dab, ma0, R, Ca0, t, i, valor_final = 0):
    for n in range(1, i+1):
        somatorio = (1/(n*n))*(exp(-Dab*n*n*pi*pi*t/(R*R)))
        print(f"{somatorio:e}")
        soma = somatorio*6/(pi*pi)
        valor_final = soma + valor_final
    return valor_final


def razao(Dab, ma0, R, Ca0, t, i, valor_final = 0):
    for n in range(1, i+1):
        somatorio = (1/(n*n))*(exp(-Dab*n*n*pi*pi*t/(R*R)))
        print(f"{somatorio:e}")
        soma = somatorio*6/(pi*pi)
        valor_final = soma + valor_final
    return valor_final


def plota_grafico(vetor_r, valores_concen, t):
    import matplotlib.pyplot as plt
    plt.plot(vetor_r,valores_concen)
    plt.ylabel('Concentração')
    plt.xlabel('Raio')
    plt.show()


def perfil_concentracao(Dab, ma0, R, Ca0, t, i, vetor_r):
    soma = 0
    valor_grafico_concentracao = []
    for r in vetor_r:
        if r != 0:
            for n in range(1, i+1):
                somatorio = (sin((n*pi*r)/R))*(1/n)*((-1)**n)*(exp(-Dab*n*n*pi*pi*t/(R*R)))
                soma = soma + somatorio
                print(soma)
            Y = (2*R/(pi*r))*soma + 1
            print(f"Valor soma r != 0: {soma}")
        else:
            for n in range(1, i+1):
                somatorio = raio_zero(Dab, ma0, R, Ca0, t, i, n)
                soma = soma + somatorio
            Y = soma*2 + 1
        Ca = Ca0-Ca0*Y
        print(Ca)
        valor_grafico_concentracao.append(Ca)
        soma = 0
    plota_grafico(vetor_r, valor_grafico_concentracao, t)


def raio_zero(Dab, ma0, R, Ca0, t, i, n):
    return ((-1)**n)*(exp(-Dab*n*n*pi*pi*t/(R*R)))


def main():
    Dab = 3*10**-7 # [cm²/s]
    ma0 = 10 # [mg]
    R = 0.326 # [cm]    
    Ca0 = 68.9 # [mg/cm³]
            # [s] - [admensio]
    vetor_tempo = [18, 180, 1800, 3600, 7200, 10800, 14400, 18000, 21600, 24*3600] # [s]
    vetor_r = [0, 0.0001, 0.05, 0.1, 0.15, 0.20, 0.25, 0.30, 0.326]
    n = 26
    for t in vetor_tempo:
        print(f"Temos: {(t/3600):.3f} horas")
        razao_ = razao(Dab, ma0, R, Ca0, t, n)
        print(f"ma(t)/ma0(t) = {razao_:e}")
        print(f"1 - ma(t)/ma0(t) = {(1-razao_):e}")
        print()
    t = 3*3600
    perfil_concentracao(Dab, ma0, R, Ca0, t, n, vetor_r)


if __name__ == "__main__":
    main()


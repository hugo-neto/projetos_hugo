
import numpy as np
import matplotlib.pyplot as plt

# Vetores para armazenar valores que serão plotados no gráfico
x1_v, x2_v, h_v = [], [], []


def f1(x1, x2, F):
    total = ((0.53)*(x1)*(x2))/(0.12 + x2) - ((F/10) + 0.01)*x1
    return total


def f2(x1, x2, F):
    total = (F/10)*(4-x2) - (2.5)*((0.53*x1*x2)/(0.12 + x2))
    return total


def plota_grafico(x_v, h_v, texto="xi"):
    #[a,b (intervalo a,b) ,nº de subdivisões]
    fig, ax = plt.subplots()

    line1, = ax.plot(h_v, x_v, label=f'Variação da C de {texto} em função do tempo')
    #line1.set_dashes([2, 6, 2, 6])  # 2pt line, 2pt break, 10pt line, 2pt break

    # Using plot(..., dashes=...) to set the dashing when creating a line
    #line2, = ax.plot(h_v, x2_v , dashes=[4, 6], label='Variação da C do Substrato em função do tempo')

    #Linha referente à legenda no canto do gráfico
    ax.legend()
    #Mostrar/Plotar o gráfico
    plt.show()


def main():
    
    condicao = True
    while condicao == True:
        print("Caso deseje parar o loop, digite '0'")
        F = float(input("Digite a vazão F em [m³/h]: "))
        if F == 0:
            break
        h = 0.1
        # ua = u antes
        # u = u do presente momento
        ua1, ua2 = 1.65, 0.2

        h_v.append(0.0), x1_v.append(ua1), x2_v.append(ua2)

        k = 0

        while h <= 30.1:
            # gij; i = índice g; j = Céluas (1) ou Substrato (2)
            hp = 0.1
            g11 = hp*f1(ua1, ua2, F)

            aux = 0.5*g11 + ua1
            g21 = hp*f1(aux, ua2, F)

            aux = 0.5*g21 + ua1
            g31 = hp*f1(aux, ua2, F)

            aux = ua1 + g31      
            g41 = hp*f1(aux, ua2, F)
            u1 = ua1 + (1/6)*(g11 + 2*g21 + 2*g31 + g41)

        # ---------------------------------------------------------------------- #

            g12 = hp*f2(ua1, ua2, F)

            aux = 0.5*g12 + ua2
            g22 = hp*f2(ua1, aux, F)

            aux = 0.5*g22 + ua2
            g32 = hp*f2(ua1, aux, F)

            aux = ua2 + g32
            g42 = hp*f2(ua1, aux, F)
            u2 = ua2 + (1/6)*(g12 + 2*g22 + 2*g32 + g42)

            x1_v.append(u1)
            x2_v.append(u2)
            h_v.append(h)

            k = k + 1
            print(f"Entrou com x1: {ua1}")
            print(f"Entrou com x2: {ua2}")
            print(f"Interação número {k}")

            h = h + 0.1
            ua1 = u1
            ua2 = u2

        plota_grafico(x1_v, h_v, "Células")
        plota_grafico(x2_v, h_v, "Substrato")


if __name__=='__main__':
    main()

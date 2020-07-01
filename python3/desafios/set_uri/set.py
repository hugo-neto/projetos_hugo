# -*- coding: utf-8 -*-
LINK DESAFIO: https://www.urionlinejudge.com.br/judge/pt/problems/view/1090


def apaga(cont1, cont2, lista):
    del lista[cont2], lista[cont1], lista[0]
    return lista


def filtra(contador, fig_t, num_t):
    lastro_fig, lastro_num, lastro_tam = fig_t[0], num_t[0], len(fig_t)
    
    for j in range(1, lastro_tam):
        if (lastro_fig == fig_t[j]):
            if (lastro_num != num_t[j]):
                for k in range(j + 1,lastro_tam):
                    if (fig_t[j] == fig_t[k]) and (num_t[j] != num_t[k]) and (lastro_num != num_t[j]):
                        fig_t, num_t = apaga(j, k, fig_t), apaga(j, k, num_t)
                        return contador + 1

        
            elif (lastro_num == num_t[j]):
                for k in range(j + 1,lastro_tam):
                    if (fig_t[j] == fig_t[k]) and (num_t[j] == num_t[k]):
                        fig_t, num_t = apaga(j, k, fig_t), apaga(j, k, num_t)
                        return contador + 1

        else:
            if (lastro_num != num_t[j]):
                for k in range(j + 1,lastro_tam):
                    if (fig_t[j] != fig_t[k]) and (lastro_fig != fig_t[k]) and (num_t[j] != num_t[k]) and (lastro_num != num_t[k]):
                        fig_t, num_t = apaga(j, k, fig_t), apaga(j, k, num_t)
                        return contador + 1                                    
    return contador


if __name__=='__main__': 
    n = int(input("Digite n: "))
    while n != 0:     
        fig_t, num_t, contador = [], [], 0
        for i in range(0,int(n)):
            texto = input("")
            texto = texto.split()
            fig_t.append(texto[1].replace('s',''))
            num_t.append(texto[0])
            if len(fig_t) >= 3:
                contador = filtra(contador, fig_t, num_t)
        print(f"Total de sets: {contador}")
        n = int(input(""))

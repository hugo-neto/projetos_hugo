y = [-0.4, 0.4, 0.5, 0.4]
x = [-0.5, 0.5, 1, 2]
p = []


def interpoladores_lagrange(xe, x, y, p):
    for i in range(0,4):
        p.append(1)
        for j in range(0,4):
            if i != j:
                p[i] = (p[i])*((xe - x[j])/(x[i] - x[j]))


def calcula_funcao(xe, x, y, p):
    final = float(0)
    for k in range(0,len(x)):
        final = final + p[k]*y[k]

    p = []
    return final


def main(xe, x, y, p):
    interpoladores_lagrange(xe, x, y, p)
    final = calcula_funcao(xe, x, y, p)
    print(final)
    print(p)


if __name__== '__main__':
    xe = 1.2   
    main(xe, x, y, p)

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols("x")
def funcao(x):
    return x**2 - 2*x + 3

d1 = sp.diff(funcao(x), x)
d2 = sp.diff(d1, x)

def Newton(funcao, X0, d1, d2, erro = 1e-5, maxit = 100):
    
    cit = 0
    de1 = d1.subs(x, X0)
    de2 = d2.subs(x, X0)
    X1 = X0 - (de1/de2)
    while abs(X1 - X0) > erro and cit < maxit:
        
        de1 = d1.subs(x, X0)
        de2 = d2.subs(x, X0)

        X1 = X0 - (de1/de2)
        X0 = X1

        cit += 1
        print('X0: ', X0, 'X1: ', X1, 'iteração: ', cit)
    return X1
X0 = float(input("Digite o valor inicial X0: "))

XM = Newton(funcao,X0,d1,d2)

print(f"O ponto de mínimo dessa função é {XM}")

print(f"A derivada a primeira é {d1}")

print(f'A derivada a segunda é {d2}')

print(f'O valor de {XM} aplicado na função resulta em: {funcao(XM)}')

x = np.linspace(-100,100,1000)
plt.plot(XM, funcao(XM), "bo")
plt.plot(x, funcao(x), color = 'blue')
plt.show()
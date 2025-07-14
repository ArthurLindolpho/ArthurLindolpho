import matplotlib.pyplot as plt
import numpy as np

def funcao(x):
    return x ** 2 - 6 * x + 15
#O usuário pode mudar a equação caso deseje e o número de iterações.
def aurea(funcao, Xl, Xh, erro = 1e-5, max_iterações = 100):

    fi = 0.618
    X1 = Xh - 0.618 * (Xh - Xl)
    X2 = Xl + 0.618 * (Xh - Xl)
    f1 = funcao(X1)
    f2 = funcao(X2)
    cit = 0

    while abs(Xh - Xl) > erro and cit < max_iterações:


        if f1 < f2:
            Xl = Xl
            Xh = X2
            X2 = X1
            f2 = f1
            X1 = Xh - 0.618 * (Xh - Xl)
            f1 = funcao(X1)
        else:
            Xh = Xh
            Xl = X1
            X1 = X2
            f1 = f2
            X2 = Xl + 0.618 * (Xh - Xl)
            f2 = funcao(X2)

        cit += 1

    if f1 < f2:
        return X1, f1
    else:
        return X2, f2

Xh = float(input("Digite o limite superior do intervalo:"))
Xl = float(input("Digite o limite inferior do intervalo:"))


Min , val_min = aurea(funcao,Xl,Xh)

x = np.linspace(-100, 100, 1000)
plt.plot(Min,funcao(Min), "bo")
plt.plot(x,funcao(x), color = "blue")
plt.show()
print(f"O ponto de mínimo dessa função é x = {Min}")
print(f"O valor da função nesse ponto é f(x) = {val_min}")
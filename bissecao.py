import matplotlib.pyplot as plt

def func(x):
    return 3*x**3 + 2*x**2 - 2

def bissecao(a, b, e = 0.00001, max_it = 100):
    cont = 0
    if func(a) * func(b) > 0:
        print(f'Não existe garantia de raiz dentro do intervalo [{a}, {b}]')
        return 
    
    while abs(b - a) > e and cont < max_it:
        c = (a+b)/2
        if func(c) == 0:
            return c

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c 
        cont += 1
    return (a+b)/2

print(f'O valor obtido a partir do método da bisseção foi: {bissecao(-1,1)}')
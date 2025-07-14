from sympy import symbols, diff

x1, x2, lmb = symbols("x1 x2 lmb")

f = (2*x1-2)**4 + (x1-2*x2)**2 

def minimize_newton(f, x0, direcao, e):
    
    c = f.subs({x1: x0[0] + direcao[0]*lmb, x2: x0[1] + direcao[1]*lmb})
    dc1 = diff(c, lmb)
    dc2 = diff(c, lmb, 2)
    xl = 0
    xh = xl - (dc1.subs({lmb: xl})) / (dc2.subs({lmb: xl}))  # cálculo do x1 antes de entrar no laço
    k = 0
    while abs(xh - xl) > e:
        xl = xh
        xh = xl - (dc1.subs({lmb: xl})) / (dc2.subs({lmb: xl}))
        k = k + 1
        if k > 200:  # Cão de guarda para impedir muitas iterações
            break
    return float((xh + xl) / 2)

def methj(x0):
    y0 = x0[:]
    x1 = [0, 0]
    k = 0
    while k < 50:
        d1 = [1, 0]
        d2 = [0, 1]
        lambda_ = minimize_newton(f, y0, d1, 0.05)
        y1 = [y0[0] + d1[0] * lambda_, y0[1] + d1[1] * lambda_]
        lambda_ = minimize_newton(f, y1, d2, 0.05)
        y2 = [y1[0] + d2[0] * lambda_, y1[1] + d2[1] * lambda_]
        d = [y2[0] - y0[0], y2[1] - y0[1]]
        lambda_ = minimize_newton(f, y2, d, 0.05)
        x1 = [y2[0] + d[0] * lambda_, y2[1] + d[1] * lambda_]
        y0 = x1[:]
        k = k + 1
    return x1

x0 = [0, 0]
g = methj(x0)

d = f.subs({x1: g[0], x2: g[1]})
print('g = ', g)
print('d = ', d)


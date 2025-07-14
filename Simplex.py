from sympy import symbols

x1, x2 = symbols("x1 x2")

f = (1-x1)**2 + 100*(x2 - x1**2)**2

def cn(x):
    return f.subs({x1: x[0], x2: x[1]})

def simplex(y1, y2, y3, e):
    k = 0
    while k < 100:
        if cn(y1) < cn(y2) and cn(y1) < cn(y3):
            xl = y1
            if cn(y2) < cn(y3):
                xs = y2
                xn = y3
            else:
                xs = y3
                xn = y2
        elif cn(y2) < cn(y1) and cn(y2) < cn(y3):
            xl = y2
            if cn(y1) < cn(y3):
                xs = y1
                xn = y3
            else:
                xs = y3
                xn = y1
        elif cn(y3) < cn(y1) and cn(y3) < cn(y2):
            xl = y3
            if cn(y1) < cn(y2):
                xs = y1
                xn = y2
            else:
                xs = y2
                xn = y1

        f1 = cn(xn)  
        
        c = [0.5 * (xl[0] + xs[0]), 0.5 * (xl[1] + xs[1])]

        xr = [c[0] + (c[0] - xn[0]), c[1] + (c[1] - xn[1])]
        
        if cn(xr) < cn(xs) and cn(xr) > cn(xl):
            xn = xr
            y1 = xl
            y2 = xs
            y3 = xn
      
        elif cn(xr) < cn(xs) and cn(xr) < cn(xl):
            xe = [c[0] + 2 * (xr[0] - c[0]), c[1] + 2 * (xr[1] - c[1])]
            if cn(xr) < cn(xe):
                xn = xr
            else:
                xn = xe
            y1 = xl
            y2 = xs
            y3 = xn
       
        else:
            xc = [c[0] + 0.5 * (xn[0] - c[0]), c[1] + 0.5 * (xn[1] - c[1])]
            if cn(xc) < cn(xn):
                xn = xc
                y1 = xl
                y2 = xs
                y3 = xn
            
            else:
                xl = xl
                xs = [xl[0] + 0.5 * (xs[0] - xl[0]), xl[1] + 0.5 * (xs[1] - xl[1])]
                xn = [xl[0] + 0.5 * (xn[0] - xl[0]), xl[1] + 0.5 * (xn[1] - xl[1])]
                y1 = xl
                y2 = xs
                y3 = xn

        f2 = cn(xl)  
        
        if abs(f2 - f1) < e:
            break
        
        k += 1
        print(y1)
        print(y2)
        print(y3)
    
    print(k)
    return xl

y1 = [1, 2]
y2 = [1.05, 3]
y3 = [1, 3.05]

resultado = simplex(y1, y2, y3, 1e-30)
valor_final = f.subs({x1: resultado[0], x2: resultado[1]})

print("Melhor ponto:", resultado)
print("Valor da função no melhor ponto:", valor_final)

                
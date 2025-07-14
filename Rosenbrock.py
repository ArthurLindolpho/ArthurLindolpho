import numpy as np


def funcao_objetivo(x):
    
    return (x[0]-2)**4 + (x[0] - 2*x[1])**2


def busca_linear(x, d, funcao, alpha_init=1.0, tol=1e-4):
    """
    """
    alpha = alpha_init
    c = 0.5  
    while funcao(x + alpha * d) > funcao(x):
        alpha *= c
        if alpha < tol:
            break
    return alpha

def gram_schmidt(vetores):
    """
    """
    ortogonais = []
    for i, v in enumerate(vetores):
        v_ort = v - sum(np.dot(v, d) / np.dot(d, d) * d for d in ortogonais)
        v_ort = v_ort / np.linalg.norm(v_ort)
        ortogonais.append(v_ort)
    return ortogonais

def algoritmo_direcoes(funcao, x0, direcoes, erro=1e-6, max_it=100):
    x_k = np.array(x0)  
    k = 0  
    n = len(direcoes)  
    direcoes_ort = gram_schmidt(direcoes)  
    
    while k < max_it:
        for j in range(n):
            d_j = direcoes_ort[j]  
            alpha = busca_linear(x_k, d_j, funcao)
            
            x_k1 = x_k + alpha * d_j
          
            if np.linalg.norm(x_k1 - x_k) < erro:
                print(f"Convergiu em {k} iterações.")
                return x_k1
            x_k = x_k1  
            k += 1
    
    print("Número máximo de iterações atingido.")
    return x_k

direcoes = [np.array([1, 1]), np.array([1, -1])]  

x0 = np.array([0.0, 0.0])

resultado = algoritmo_direcoes(funcao_objetivo, x0, direcoes)

print("Solução encontrada:", resultado)


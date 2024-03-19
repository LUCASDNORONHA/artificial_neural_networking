import numpy as np

# Entradas
entradas = np.array([1, 7, 5])

# Pesos
pesos = np.array([0.0, 0.1, 0])

# Função para calcular a soma ponderada
def soma(e, p):
    return e.dot(p) # produto escalar (dot product)


# Função de ativação (função degrau)
def stepFunction(soma):
    if soma >= 1:
        return 1
    else:
        return 0

# Calcula a soma ponderada
s = soma(entradas, pesos)

# Aplica a função de ativação
r = stepFunction(s)

print("Resultado:", r)

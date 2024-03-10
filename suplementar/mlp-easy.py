import numpy as np

def sigmoid(u):
    return 1 / (1+np.exp(-u))

def der_sigmoid(u):
    return sigmoid(u) * (1 - sigmoid(u))


X = [3.5, 5.1, -1]
n = 0.1

w1 = [0.18, 0.49, 0.81]
w2 = [0.43, 0.82, 0.79]
w3 = [0.75, 0.13, 0.24]


# pra frente
u1 = np.matmul(X, w1)
u2 = np.matmul(X, w2)
U = [u1, u2, -1]

h = np.matmul(U, w3)
y = sigmoid(h)

d = 1
e3 = d - y

print(f'O Modelo cuspiu {round(y, 4)} e o desejado era {d}. Erro de {round(e3, 4)}.\n')

# atualizar w3 (camada de saída)
U = np.asarray(U)
w1, w2, w3 = np.asarray(w1), np.asarray(w2), np.asarray(w3)

print(f'W3 era {w3}')
print(f'W1 era {w1}')
print(f'W2 era {w2}\n\n')

w3 = w3 +  n * e3 * der_sigmoid(h) * U
print(f'W3 passou a ser {w3}, após a correção.')

# erro após atualização
ne3 = d - sigmoid(np.matmul(U, w3)) 

# atualizar w2 (camada oculta)


w2 = w2 + n * der_sigmoid(u2) * (e3 * der_sigmoid(y) * w3) * U
w1 = w1 + n * der_sigmoid(u1) * (e3 * der_sigmoid(y) * w3) * U

print(f'W1 passou a ser {w1}, após a correção.')
print(f'W2 passou a ser {w2}, após a correção.')



# pra frente
u1 = np.matmul(X, w1)
u2 = np.matmul(X, w2)
U = [u1, u2, -1]

h = np.matmul(U, w3)
y = sigmoid(h)

d = 1
e3 = d - y

print(f'\nO modelo cospe agora {round(y, 4)} e o desejado era {d}. Erro de {round(e3, 4)}')

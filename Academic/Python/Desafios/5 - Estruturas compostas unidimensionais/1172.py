# inicializando com uma lista vazia
X = []

# lendo os 10 valores para o vetor
for i in range(10):
    valor = int(input())
    X.append(valor) # adicionando o valor ao "vetor x"
    
# substituindo valores nulos e negativos por 1
for i in range(10):
    if X[i] <= 0:
        X[i] = 1

# imprimindo os 10 valores
for i in range(10):
    print(f"X[{i}] = {X[i]}")
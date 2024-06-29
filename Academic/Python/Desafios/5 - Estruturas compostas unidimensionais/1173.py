# inicializa o vetor N com o tamanho 10
N = [0] * 10

valor = int(input())

# coloca o valor lido na primeira posição do vetor
N[0] = valor

for i in range(1, 10):
    # garante que cada posição subsequente tenha o dobro do valor da posição anterior
    N[i] = N[i - 1] * 2
    
for i in range(10):
    print(f"N[{i}] = {N[i]}")
X = float(input())

N = [0] * 100  # inicializa o vetor N com 100 posições

N[0] = X  # coloca o valor X na primeira posição

# preenche as posições de 1 até 99 conforme especificado
for i in range(1, 100):
    N[i] = N[i-1] / 2.0

# imprime o vetor N formatado
for i in range(100):
    print(f"N[{i}] = {N[i]:.4f}")

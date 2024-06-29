T = int(input())

N = [0] * 1000

for i in range(1000):
    N[i] = i % T # O operador módulo i % T retorna o resto da divisão de i por T. Isso significa que os valores gerados por i % T estarão sempre no intervalo de 0 até T-1.
    print(f"N[{i}] = {N[i]}")



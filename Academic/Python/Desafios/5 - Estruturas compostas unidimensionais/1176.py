# lê o número de casos de testes 
T = int(input())

# lista de Fibonacci com os seus 2 primeiros valores definidos (1° e 2° termo)
fibonacci = [0, 1]

# calcula todos os valores de fibonacci do 3° até o 60° termo
for i in range(2, 61): # vai de 2 até 60
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2]) # adicionado os valores para a lista 'fibonacci'

    # o valor de determinado termo será a soma dos seus valores antecessores 
    # ex: fibonacci[2] = fibonacci[2-1] + fibonacci[2-2]
    # fibonacci[2] = fibonacci[1] + fibonacci[0]
    # fibonacci[2] = 0 + 1 
    # fibonacci[2] = 1 

# cria uma lista para armazendas os valores das posições
resultado = []

for _ in range(T):
    N = int(input()) # posição do valor de fibonacci
    resultado.append(f"Fib({N}) = {fibonacci[N]}")

for i in resultado: # contador que fará um loop com base no tamanho da lista 'resultado'
    print(i)

# inicia com listas vazias
par = []
impar = []

for _ in range(15):
    num = int(input())

    if num % 2 == 0:
        par.append(num) # caso o numero seja par, adicionada ao vetor 'par=[]'
    
        if len(par) == 5:
            for i in range(5):
                print(f"par[{i}] = {par[i]}") # imprime todos os valores da lista 'par=[]'
            par = [] # zera a lista
    
    else: 
        impar.append(num) # caso o numero seja impar, adicionada ao vetor 'impar=[]'

        if len(impar) == 5:
            for i in range(5):
                print(f"par[{i}] = {impar[i]}")
            impar = []        

# imprime o valor que restou de cada vetor
for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")
for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
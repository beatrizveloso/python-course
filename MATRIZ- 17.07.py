# Importando biblioteca ramdômica
import random
# definir o tamanho da matriz
TAM = 3
# definindo o laço para a matriz que
# inteira TAM vezes
mat = [[] for _ in range(TAM)]

# Entrada de valores de dados/ valores randômicos
for lin in range(TAM):
    for col in range(TAM):
        mat[lin].append(random.randrange(0,10))

# Saída de dados
print("Matriz:")
for cont in mat:
    print(cont)

# Processamento
print(f"Diagonal Principal: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin==col:
            print(f" {mat[lin][col]}")

print(f"Triângulo Superior Diagonal Principal: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin<col:
            print(f" {mat[lin][col]}")

print(f"Triângulo Inferior Diagonal Principal: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin>col<TAM-1:
            print(f" {mat[lin][col]}")

print(f"Triângulo Superior Diagonal Secundário: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin+col<TAM-1:
            print(f" {mat[lin][col]}")

print(f"Triângulo Inferior Diagonal Secundário: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin+col>TAM-1:
            print(f" {mat[lin][col]}")

print(f"Diagonal Secundário: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin+col==TAM-1:
            print(f" {mat[lin][col]}")
        

    
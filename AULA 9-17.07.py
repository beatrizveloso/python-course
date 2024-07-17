# Aula de Matrizes
# Importando biblioteca ramdômica

import random

# definir o tamanho da matriz
TAM = 50

# definindo o laço para a matriz que
# inteira TAM vezes
mat1 = [[] for _ in range(TAM)]
mat2 = [[] for _ in range(TAM)]
mat3 = [[0 for _ in range(TAM)] for _ in range(TAM)]

# Função soma
def soma():
    for lin in range(TAM):
        for col in range(TAM):
            mat3[lin][col]= (mat1[lin][col] + mat2[lin][col])

# Função subtração
def sub():
    for lin in range(TAM):
        for col in range(TAM):
            mat3[lin][col]= (mat1[lin][col] - mat2[lin][col])

# Função multiplicação
def mult():
    for lin in range(TAM):
        for col in range(TAM):
            mat3[lin][col]= (mat1[lin][col] * mat2[lin][col])

# Preenchendo a matriz com números aleatórios
for lin in range(TAM):
    for col in range(TAM):
        mat1[lin].append(random.randrange(0,10))
        mat2[lin].append(random.randrange(0,10))

# para exibir
print("Matriz 1: ")
for cont in mat1:
    print(cont)

print("Matriz 2: ")
for cont in mat2:
    print(cont)

resp = input("Escolha sua operação: ")

print("Matriz Soma: ")
soma()
for cont in mat3:
    print(cont)

print("Matriz Subtração: ")
sub()
for cont in mat3:
    print(cont)

print("Matriz Multiplicação: ")
mult()
for cont in mat3:
    print(cont)

#Função
#1. Elabore uma função que retorne
# A soma do dois números 
def soma(num1, num2):
    return num1 + num2

def dif(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num1==0 or num2==0:
        print("Não existe divisão por 0")
    else:
        return num1 / num2

n1 = int(input("N1: "))
n2 = int(input("N2: "))
resp = int(input("Escolha: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisãp\n\nEscolha sua operação: "))

if resp == 1:
    res = soma(n1,n2)
    print(f"Soma: é {res}")

elif resp == 2:
    res = dif(n1,n2)
    print(f"Subtração: {res}")

elif resp == 3:
    print(f"Multiplicação: ", mult(n1,n2))

elif resp == 4:
    print(f"Divisão {div(n1,n2)}")

else:
    print("Opção Inválida")
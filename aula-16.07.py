#Função
#1. Elabore uma função que retorne
# A soma do dois números 
def soma(num1, num2):
    return num1 + num2

n1 = int(input("N1: "))
n2 = int(input("N2: "))
res = soma(n1,n2)
print(f"Soma: é {res}")
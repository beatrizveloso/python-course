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
    
def pot(num1, num2):
    return num1 ** num2

def resto(num1, num2):
    if num1==0 or num2==0:
        print("Não existe divisão por 0")
    else:
        return num1%num2
    
def parImpar(num1):
    if num1%2 == 0:
        return 1
    else: 
        return 0
    
def primo(num1):
    for cont in range(1,num1+1):
        if num1%cont ==0:
            contDiv=+1
        if contDiv <= 2:
            return 1
        else:
            return 0
        
def fatorial(num1):
    fat = 1
    for cont in range(1,num1+1):
        fat*=cont
    return fat

def tabuada(num1):
    for cont in range(1,11):
        tab = num1 * cont
        print(f"{num1} * {cont} = {tab}")


resp = int(input("Escolha: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisãp\n5 - Exponenciação\n6 - Resto de divisão\n7 - Par ou Ímpar\n8 - Primo\n9 - Fatoria\n10 - Tabuada\n0 - Sair \n\nEscolha sua operação: "))

n1 = int(input("N1: "))
n2 = int(input("N2: "))

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

elif resp == 5:
    print(f"Exponenciação: {pot(n1,n2)}")

elif resp == 6:
    print(f"Resto da divisão é:  {resto(n1,n2)}")

elif resp == 7:
    if parImpar(n1) == 1:
        print(f"{n1} é PAR")
    elif parImpar(n1) == 0:
        print(f"{n1} é ÍMPAR") 
    if parImpar(n2) == 1:
        print(f"{n2} é PAR")
    elif parImpar(n2) == 0:
        print(f"{n2} é ÍMPAR") 

elif resp == 8:
    if primo(n1) == 1 and primo(n2) == 1:
        print(f"{n1} e {n2} são primos")
    elif primo(n1) == 1 and primo(n2) == 0:
        print(f"{n1} é primo e {n2} não é primo")
    elif primo(n1) == 0 and primo(n2) == 1:
        print(f"{n1} não é primo e {n2} é primo")
    elif primo(n1) == 0 and primo(n2) == 1:
        print(f"{n1} e {n2} não são primos")

elif resp == 9:
    print(f"Fatorial de {n1}:  {fatorial(n1)}")
    print(f"Fatorial de {n2}:  {fatorial(n2)}")

elif resp == 10:
    tabuada(n1)
    tabuada(n2)

else:
    print("Opção Inválida")
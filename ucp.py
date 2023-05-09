import os

os.system("cls")

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i])*pow(2,len(binary)-1-i)
    return decimal

def decimal_to_binary(decimal):
    binary = []
    while decimal!= 0:
        binary.append(str(decimal % 2))
        decimal = decimal // 2
    return binary [::-1]

def switch_case(num):
    if num == 1:
        os.system("cls")
        elemento = int(input("Decimal: "))
        resultado = decimal_to_binary(elemento)
        resultado = " ".join(resultado)
        resultado = print(resultado)
        return resultado
    
    elif num == 2:
        os.system("cls")
        elemento = input("Binário: ")
        resultado = print(binary_to_decimal(elemento))
        return resultado
    
    else:
        return 0

conversao = int(input("Menu:\n\n0 = Sair\n1 = Decimal -> Binário\n2 = Binário -> Decimal\n\n"))

switch_case(conversao)

# Grupo 3: Carlos Lacerda, Samuel, Valter, Vinicius Lorencio;
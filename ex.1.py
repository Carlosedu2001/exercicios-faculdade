import os

os.system("cls")

lerNum = []
num = 0
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

while num >= 0:
    num = int(input('Digite um número: '))
    lerNum.append(num)

os.system("cls")

for i in lerNum:
    if i >= 0 and i <= 25:
        lista1.append(i)
    elif i > 25 and i <= 50:
        lista2.append(i)
    elif i > 50 and i <= 75:
        lista3.append(i)
    elif i > 75 and i <= 100:
        lista4.append(i)
        i = 0
    elif i > 100:
        lista5.append(i)

print(f'Os números de 0 a 25 são: {lista1}, total: {len(lista1)}')
print(f'Os números de 26 a 50 são: {lista2}, total: {len(lista2)}')
print(f'Os números de 51 a 75 são: {lista3}, total: {len(lista3)}')
print(f'Os números de 76 a 100 são: {lista4}, total: {len(lista4)}')
print(f'Os números acima de 100 são: {lista5}, total: {len(lista5)}')
import os

os.system("cls")

num = 0
notas = []
media = 0

while num >= 0:
    num = float(input("Digite uma nota: "))
    notas.append(num)

notas.pop()
print(notas)

for i in notas:
    media = media + i

media = media / len(notas) 
   
print(media)
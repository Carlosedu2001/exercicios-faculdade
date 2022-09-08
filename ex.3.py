import os

os.system("cls")

num = 0
idade = []
jovem = []
adulta = []
idosa = []
media = 0

print("Para sair digite um número menor que 0\n")

while num >= 0:
    num = int(input("Digite uma idade: "))
    idade.append(num)

idade.pop()

for i in idade:
    if i <= 25:
        jovem.append(i)
    elif i <= 60:
        adulta.append(i)
    else:
        idosa.append(i)

if len(jovem) == len(adulta) and len(jovem) == len(idosa):
    print("\nHá o mesmo número de pessoas em cada turma (jovem: 0-25, adulta: 26-60 e idosa: 60+)")
elif len(jovem) > len(adulta) and len(jovem) > len(idosa):
    print("\nA turma é em média jovem")
elif len(adulta) > len(idosa):
    print("\nA turma é em média adulta")
else:
    print("\nA turma é em média idosa")
for i in idade:
    media = media + i

media = media / len(idade)

print(f"\nA média de idade da turma é: {media}")

if media <= 25:
    print("\nA turma é jovem")
elif media <= 60:
    print("\nA turma é adulta")
else:
    print("\nA turma é idosa")
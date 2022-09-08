import os

os.system("cls")

voto = ''
a = 0
b = 0
c = 0
vazio = 0

print("Digite 'SAIR' para sair\n")
while voto != 'SAIR':
    voto = str.upper((input("Digite a letra correspondente ao seu voto: ")))

    if voto == 'A':
        a = a + 1
    elif voto == 'B':
        b = b + 1
    elif voto == 'C':
        c = c + 1
    else:
        vazio = vazio + 1

os.system("cls")

if a == b and a == c:
    print(f"Houve um empate.\nA = {a}\tB = {b}\tC = {c}")
elif a > b and a > c and a > vazio:
    print(f"O candidato A venceu a eleição.\nA = {a}\tB = {b}\tC = {c}")
elif b > a and b > c and b > vazio:
    print(f"O candidato B venceu a eleição.\nA = {a}\tB = {b}\tC = {c}")
else:
    print(f"O candidato C venceu a eleição.\nA = {a}\tB = {b}\tC = {c}")

print(f"\nTotal de votos em branco: {vazio-1}\n")
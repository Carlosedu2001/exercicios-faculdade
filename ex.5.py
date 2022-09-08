import os

os.system("cls")

media = 0

while media != 9 and media >= 0 and media <= 10:
    n1 = float(input("Digite sua 1ª nota: "))
    n2 = float(input("Digite sua 2ª nota: "))
    n3 = float(input("Digite sua 3ª nota: "))
    media = (n1 + n2 + n3) / 3

    print(media)

    if media < 0 or media > 10:
        print("\nAlgo deu errado, tente novamente...\n")
    elif media >= 7 and media < 10:
        print("\nAprovado\n")
    elif media < 7 and media >= 0:
        print("\nReprovado\n")
    else:
        print("\nAprovado com Distinção\n")
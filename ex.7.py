import os

os.system("cls")

regiao = ''

print("Digite 'FIM' em região e qualquer número para os meses para sair\n")

while regiao != "FIM":
    regiao = str.upper(input("Digite o nome da região: "))
    janeiro = float(input("Digite o valor das vendas de Janeiro: "))
    fevereiro = float(input("Digite o valor das vendas de Fevereiro: "))
    marco = float(input("Digite o valor das vendas de Março: "))
    abril = float(input("Digite o valor das vendas de Abril: "))

    if regiao != "FIM":
        fevereiro = fevereiro * 4
        abril = abril * 4

        media = (janeiro + fevereiro + marco + abril) / 4

        print(f"\nAs vendas da região {regiao} foram:\nJaneiro: R${janeiro} \t Fevereiro: R${fevereiro} \t Março: R${marco} \t Abril: R${abril}\n\nMédia: R${media}\n")
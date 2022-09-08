import os

os.system("cls")

cidade = ''

print("Para sair digite 'FIM' em cidade e qualquer número em temperatura\n")

while cidade != "FIM":
    cidade = str.upper(input("Digite o nome da cidade: "))
    temperatura = float(input("Digite a temperatura em Celsius: "))
    if cidade != 'FIM':
        temperatura = (9*temperatura+160) / 5

        print(f"\nA temperatura de {cidade} em Fahrenheit é de {temperatura}°F\n")
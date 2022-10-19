import os

os.system("cls")

request = ''

email = 'aluno@hotmail.com'
senha = 'aluno123'

verifica_email = ''
verifica_senha = ''

while verifica_email.upper() != "SAIR" or verifica_senha.upper() != "SAIR":

    verifica_email = str(input("Digite seu email: "))

    if '@' in verifica_email and '.com' in verifica_email or '.com.br' in verifica_email or '.br' in verifica_email and not ' ' in verifica_email:
        print("Email liberado\n")
    else:
        print("Endereço de email fora das regras\n")

    verifica_senha = str(input("Digite sua senha (6 ou mais caracteres): "))

    if verifica_senha.__len__() >= 6 and not ' ' in verifica_senha:
        print("Senha liberada\n")
    else:
        print("Senha inválida\n")

os.system("cls")
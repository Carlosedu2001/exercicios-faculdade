import os
import re

os.system("cls")

sair = 0

emails = ''
senhas = ''

usuario = {
    "email": [],
    "senha": []
    }

def remove_acento_caractere_especial(letras):
        letras = re.sub('á','a', letras)
        letras = re.sub('é','e', letras)
        letras = re.sub('í','i', letras)
        letras = re.sub('ó','o', letras)
        letras = re.sub('ú','u', letras)
        letras = re.sub('ý','y', letras)
        letras = re.sub('à','a', letras)
        letras = re.sub('è','e', letras)
        letras = re.sub('ì','i', letras)
        letras = re.sub('ò','o', letras)
        letras = re.sub('ù','u', letras)
        letras = re.sub('ä','a', letras)
        letras = re.sub('ë','e', letras)
        letras = re.sub('ï','i', letras)
        letras = re.sub('ö','o', letras)
        letras = re.sub('ü','u', letras)
        letras = re.sub('ÿ','y', letras)
        letras = re.sub('â','a', letras)
        letras = re.sub('ê','e', letras)
        letras = re.sub('î','i', letras)
        letras = re.sub('ô','o', letras)
        letras = re.sub('û','u', letras)
        letras = re.sub('ã','a', letras)
        letras = re.sub('õ','o', letras)
        letras = letras.replace('@', 'ABC123ABC')
        letras = letras.replace('.', '123ABC123')
        letras = "".join(c for c in letras if c.isalnum())
        letras = letras.replace('ABC123ABC', '@')
        letras = letras.replace('123ABC123', '.')
        return letras

while sair != 2:
    
    emails = (str(input("Digite seu email: ")))
    emails = remove_acento_caractere_especial(emails)
    if '@' in emails and '.com' in emails or '.com.br' in emails or '.br' in emails and not ' ' in emails and emails.__len__() > 5 and emails.__len__() <= 40:
        usuario["email"].append(emails)
        print("Email liberado\n")
    else:
        print("Endereço de email fora das regras\n")

    senhas = (str(input("Digite sua senha: ")))
    if senhas.__len__() >= 6 and senhas.__len__() <= 20 and not ' ' in senhas:
        usuario["senha"].append(senhas)
        print("Senha liberada\n")
    else:
        print("Senha inválida\n")
    
    sair = int(input(f"1 - SIM\n2 - NÃO\nDeseja continuar?  "))
    
    if sair != 1 and sair != 2:
        os.system("cls")
        print("Valor inválido")
        print(usuario)
        exit()

    os.system("cls")

print(usuario)

# VERSÃO ALTERNATIVA DO TRABALHO DE MANEIRA MAIS FÁCIL E EFICIENTE UTILIZANDO BIBLIOTECA "re".

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# def check(verifica_email):

#     if(re.fullmatch(regex, verifica_email)):
#         print("\nEmail válido")
 
#     else:
#         print("\nEmail inválido")

# email_da_pessoa = str(input("Digite seu email: "))
# check(email_da_pessoa)
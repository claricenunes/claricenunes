# usando funções em python para gerador de senhas
import random 
import string   #biblioteca de strings

def password_generator(Len_password = 8):       #dentro do (parametros)
    ascii_options = string.ascii_lowercase  #letras minusculas
    number_options = string.digits  #numeros
    punt_options = string.punctuation  #caracteres especiais
    options = ascii_options + number_options + punt_options  #juntando todas as opcoes

    password_user = ""

    for i in range (0, Len_password):  #para cada digito no intervalo de 0 ate o tamanho da senha 
        digit = random.choice(options)  #escolha aleatoria das opcoes
        password_user += digit  #adiciona o digito a senha

    return password_user  #retorna a senha

choice_user = input('Quantos digitos tem a sua senha? ')  #input do usuario
if choice_user.isdigit():  #verifica se o input e um digito
    choice_user = int(choice_user)
else:
    print("Entrada inválida!")
    quit()

response = password_generator(Len_password=choice_user)
print(f'Senha gerada:\n{response}')
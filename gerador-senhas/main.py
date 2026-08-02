import string
import secrets

def gerarSenha(força, tamanho):
    letras = string.ascii_letters
    digitos = string.digits
    simbolos = string.punctuation
    if força == "forte":
        forte = letras + digitos + simbolos
        senha = ''.join((secrets.choice(forte) for i in range(tamanho)))
    elif força == "media":
        media = letras + digitos
        senha = ''.join((secrets.choice(media) for i in range(tamanho)))
    else:
        senha = ''.join((secrets.choice(letras) for i in range(tamanho)))
    
    return "Sua nova senha é: " + senha

def main():
    print("Olá! Seja bem-vindo ao gerador de senhas aleatórias!")
    força = input("Por favor, informe quão forte você quer que a senha seja (forte, media ou fraca): ").lower()
    tamanho = int(input("Por favor, informe o tamanho que você deseja para sua senha: "))
    print(gerarSenha(força, tamanho))

if __name__ == '__main__':
    main()

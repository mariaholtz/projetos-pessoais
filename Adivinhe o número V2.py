import random
inicio, fim = map(int, input('Informe o intervalo para adivinhação: ').split())
a = int(input('Adivinhe o número: '))

def guess(a, inicio, fim):
    n = random.randint(inicio, fim)
    i = 1
    while a != n:
        if n > a:
            print('O seu número é menor, tente de novo!')
        elif n < a:
            print('O seu númeor é muito grande, tente de novo!')
        a = int(input('Adivinhe o número: '))
        i += 1
        if i > 9:
            print(f'Acabou suas tentativas. O número era {n}. Mais sorte da próxima vez!')
            break
    else:
        print(f'Parabéns! Você acertou em {i} tentativas!')

guess(a, inicio, fim)

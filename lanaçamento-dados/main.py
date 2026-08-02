import random
rolls = input('Deseja lançar os dados? (sim/nao) ')

def lançamento(rolls):
    n = 0
    while rolls == 'sim':
        dice = [random.randint(1, 6), random.randint(1, 6)]
        print(dice)
        n += 1
        rolls = input('Deseja lançar os dados? (sim/nao) ')
    print(f'Você lançou os dados {n} vezes!')

lançamento(rolls)

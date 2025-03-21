'''Write a program that simulates rolling a pair of dice. Each time the program runs, it
should randomly generate two numbers between 1 and 6 (inclusive), representing
the result of each die. The program should then display the results and ask if the
user would like to roll again.'''

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

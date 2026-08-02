import random
import emoji 

jogar = input('Quer jogar um jogo? (sim/nao) ')
player = input('Escolha entre pedra (p), papel (pl) e tesoura (t): ')
v = 0
d = 0
e = 0

while jogar == 'sim':

    es = 'p', 'pl', 't'
    computer = random.choice(es)

    op = {'p': emoji.emojize(':brick:'), 'pl': emoji.emojize(':scroll:'), 't': emoji.emojize(':scissors:')}

    if player == computer:
        print("Empate!")
        e+=1
    elif player == 'p' and computer == 'pl':

        print(f'Você escolheu {op['p']} \n' +
            f'O computador escolheu {op['pl']} \n'+
            'Você perdeu!')
        d+=1
        
    elif player == 'pl' and computer == 'p':

        print(f'Você escolheu {op['pl']} \n' +
            f'O computador escolheu {op['p']} \n'+
            'Você ganhou!')
        v+=1

    elif player == 't' and computer == 'p':

        print(f'Você escolheu {op['t']} \n' +
            f'O computador escolheu {op['p']} \n' +
            'Você perdeu!')
        d+=1

    elif player == 'p' and computer == 't':

        print(f'Você escolheu {op['p']} \n' +
            f'O computador escolheu {op['t']} \n' +
            'Você ganhou!')
        v+=1

    elif player == 'pl' and computer == 't':

        print(f'Você escolheu {op['pl']} \n' +
            f'O computador escolheu {op['t']} \n' +
            'Você perdeu!')
        d+=1

    elif player == 't' and computer == 'pl':

        print(f'Você escolheu {op['t']} \n' +
            f'O computador escolheu {op['pl']} \n' +
            'Você ganhou!')
        v+=1

    else:

        print('Inválido.')

    jogar = input('Quer jogar novamente? (sim/nao) ')
    if jogar == 'sim':

        player = input('Escolha entre pedra (p), papel (pl) e tesoura (t): ')
        
    elif jogar == 'nao':

        print('Fim de jogo! Foi muito legal, nos vemos na próxima!')
        print(f'Você tem {v} vitórias, {d} derrotas e {e} empates.')
        break

    else:

        print('Opa, acho que não entendi. Tente novamente!')
else:
    print('Tudo bem, espero que você queira jogar depois!')

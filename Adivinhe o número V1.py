import random
import time

def guess(a):
    try:
        tentativas = 10
        n = random.randint(1, 100)
        i = 1
        while a != n:
            if n > a:
                print('Seu palpite foi menor que o número. Tente novamente!')
                tentativas -= 1
                print(f'Tentativas restantes: {tentativas}\n')
            elif n < a:
                print('Seu palpite foi maior que o número. Tente novamente!')
                tentativas -= 1
                print(f'Tentativas restantes: {tentativas}\n')

            a = int(input('Dê outro palpite: '))
            i += 1
            if i == 10:
                print(f'Acabou suas tentativas. O número era {n}. Mais sorte da próxima vez!\n')
                novamente = input('Quer jogar novamente? ').lower()
                if novamente == 'sim':
                    main()
                else:
                    print('---------------------------------------------------')
                    print('BOM JOGO! NOS VEMOS NA PRÓXIMA!')
                    time.sleep(4)
                    break
        else:
            print(f'Parabéns! Você acertou em {i} tentativas!')
            novamente = input('Quer jogar novamente? ').lower()
            if novamente == 'sim':
                main()
            else:
                print('---------------------------------------------------')
                print('BOM JOGO! NOS VEMOS NA PRÓXIMA!')
                time.sleep(2)


    except Exception as error:
        print("Ocorreu o seguinte erro: ", error)
        time.sleep(4)
        novamente = input('Quer jogar novamente? ').lower()
        if novamente == 'sim':
            main()
        else:
            print('---------------------------------------------------')
            print('ATÉ LOGO!')
            time.sleep(4)



def main():
    try:
        print("\nSEJA MUITO BEM-VINDO!")
        print("O seu objetivo é adivinhar o número! Você tem 10 tentativas! \n")
        a = int(input('Dê um palpite (entre 1 e 100): '))
        guess(a)
    except Exception as error:
        print("Ocorreu o seguinte erro: ", error)
        novamente = input('Quer jogar novamente? ').lower()
        if novamente == 'sim':
            main()
        else:
            print('---------------------------------------------------')
            print('ATÉ LOGO!')
            time.sleep(4)

if __name__ == '__main__':
    main()  

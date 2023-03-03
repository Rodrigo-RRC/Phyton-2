#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('PAPEL','PEDRA', 'TESOURA')
computador = randint(0,2) # Faz o computador "PENSAR"

#print('O computador escolheu {}'.format(itens[computador]))
print('''Escolha um das opções abaixo para jogar com o computador:
[0] PAPEL
[1] PEDRA
[2] TESOURA''')
jogador = int(input('Escolha um opção: '))
print('Jô')
sleep(1)
print('Ken')
sleep(1)
print('Pow!')
sleep(1)
print('-=-' * 10)
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu a opção {}'.format(itens[jogador]))
print('-=-' * 10)

if computador == 0: # Papel
    if jogador ==0:
        print('Empate.')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Você ganhou. Parabéns!')
    else:
        print('JOGADA INVÁLIDA. REPITA O PROCESSO')
elif computador == 1: # Pedra
    if jogador == 0:
        print('Você ganhou. Parabéns!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Você perdeu.')
    else:
        print('JOGADA INVÁLIDA. REPITA O PROCESSO')
elif computador == 2:
    if jogador == 0:
        print('Você perdeu.')
    elif jogador == 1:
        print('Você ganhou. Parabéns!')
    elif jogador == 2:
        print('Empate.')
    else:
        print('JOGADA INVÁLIDA. REPITA O PROCESSO')
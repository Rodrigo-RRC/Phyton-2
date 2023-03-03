#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):

    if n % c == 0:
        print('\033[31m', end=' ')
        tot = tot + 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end='')

print('\n\033[mO número {} tem {} divisores'.format(n,tot))
if tot==2:
    print('Como o número {} tem {} dividores, ele é PRIMO.'.format(n, tot))
else:
    print('Como ele tem mais de 2 divisores, não é PRIMO.'.format(n))


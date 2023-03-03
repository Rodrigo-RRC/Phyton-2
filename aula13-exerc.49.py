from time import sleep
print('-=-' * 10)
print(' TABUABA DE UM NÚMERO NATURAL')
print('-=-' * 10)
n = int(input('Digite um número para saber a sua tabuada: '))
opçao = int(input('''Esolha uma opcão abaixo:
[1] Crianças de 5 a 7 anos
[2] Crianças de 8 a 9 anos
[3] Crianças de 9 a 11 anos
[4] Crianças maiores que 11 anos
   Opção: '''))

if opçao == 1:
    s = 4
elif opçao == 2:
    s = 3
elif opçao == 3:
    s = 2
elif opçao == 4:
    s = 1
print('Abaixo segue a tabuada do número {}'.format(n))
for c in range(1, 11):
    mult = n * c
    print(' {} x {} = {}'.format(n, c, mult))
    sleep(s)
print('Não se esqueça que isto é muito importante!')

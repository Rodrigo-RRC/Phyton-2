#Exercício Python 48: Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
#cont = 0
for n in range(1, 501):
    if n % 3 == 0 and n % 2 == 1:
       soma = soma + n
print(' A soma dos números múltiplo de 3 e ímpares no intervalo dado é: {}'.format(soma))
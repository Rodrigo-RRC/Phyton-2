#Exercício Python 47: Crie um programa que mostre na tela
# todos os números pares que estão no intervalo entre 1 e 50.

#for n in range(1, 51):
    #if n % 2 == 0:
       #print(n, end=' ')
#print('Acabou!')
## OUTRA MANEIRA #

for n in range(2, 51, 2):
     print(n, end = ' ')
     #print(n + 1)
print('ACABOU!')
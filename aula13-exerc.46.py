#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10 ,-1 , -1):
    print(c)
    sleep(1)
print('\U0001F4A3')

for d in range(0, 3):
    print('Bum! Bum! Bum!')
    sleep(1)
print('\U0001F4A3')
#print('U+1F4A3')

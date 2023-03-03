#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# an = a1 + (n-1).r
#-----------------------------------------------------------#
#a1 = int(input('Digite o Primeiro Termo (a1) de uma P.A: '))
#r = int(input('Agora digite a Razão (r) desta P.A: '))
#for n in range(1, 11):
  #an = a1 + (n-1) * r
  #print(an, end = '->')
#print('ACABOU!!!')
#------------------------------------------------------------#
# OUTRA FORMA #
a1 = int(input(' Digite o primeiro termo (a1) de uma P.A: '))
r = int(input('Agora digite a razão desta P.A: '))
a10 = a1 + (9 * r)

for c in range(a1, a10, r):
    print(c, end ='=>')
print('ACABOU!!!')
#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
print('Quer saber a soma dos números pares que você digitou?')
print('Então digite abaixo 6 números inteiros. Mãos à obra!')
soma = 0
cont = 0
for c in range(1,7):
  num = int(input('Digite o {} valor: '.format(c)))
  if num % 2 == 0:
     soma = soma + num
     cont = cont + 1
print('A quantidade de número(s) par(es) digitados foi {} e, portanto a soma será : {}'.format(cont, soma))
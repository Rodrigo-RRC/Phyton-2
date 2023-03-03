#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("Peso da {}a pessoa em Kg:".format(p)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > 1:
            maior = peso
        if peso > 1:
            menor = peso
print('O maior peso é: {}'.format(maior))
print('O menor peso é: {}'.format(menor))


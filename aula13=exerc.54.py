#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoAtual = date.today().year
totMaior = 0
totMenor = 0

for c in range(1, 8):
    pergunta = int(input('Em que ano a {}a pessoa nasceu?: '.format(c)))
    idade = anoAtual - pergunta
    if idade >= 21:
        totMaior += 1
    else:
        totMenor += 1
print('Tivemos {} pessoas que são maiores de idade'.format(totMaior))
print('E {} pessoas são menores de idade'.format(totMenor))



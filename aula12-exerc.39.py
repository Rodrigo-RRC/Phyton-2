#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoAtual = date.today().year

print('-=-'* 20)
print('       SERVIÇO DE ALISTAMENTO MILITAR OBRIGATÓRIO')
print('-=-' * 20)

anoNascimento = int(input('Digite o ano de seu nascimento: '))
anoAtual = 2023
idade = anoAtual - anoNascimento
passou = idade -18
faltam = 18 - idade

if idade == 18:
    print('Perfeito! Você tem {} anos e está pronto para se alistar!'.format(idade))
elif idade < 18:
    print('Está bem próximo para você poder se alistar. Faltam {} ano(s)'.format(faltam))
elif idade > 18:
    print(' Você perdeu o prazo de alistamento. Excedeu {} ano(s)'.format(passou))
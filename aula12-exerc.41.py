#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER
from _datetime import date
anoAtual = date.today().year
print('-=-' * 20)
print('           Confederação Nacional de Natação')
print('-=-' * 20)

anoDeNascimento = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoDeNascimento

if idade <= 9:
    print('Você tem {} anos e sua categoria será MIRIM'.format(idade))
elif 9 < idade <=14:
    print('Você tem {} anos e sua categoria será INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} anos e sua categoria será JÚNIOR'.format(idade))
elif 19 < idade <= 25:
    print('Você tem {} anos e sua categoria será SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e sua categoria será MASTER'.format(idade))

print('BOA SORTE NA COMPETIÇÃO!')

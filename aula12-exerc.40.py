#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

n1 = float(input('Digite um nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('A média foi {} e portanto o resulatdo é: REPROVADO'.format(media))
elif 5.0 <=media< 7.0:
    print('A média foi {} e portanto o resultado é: Recuperação'.format(media))
elif media >= 7.0:
    print('A média foi {} e portanto o resultado é: APROVADO'.format(media))
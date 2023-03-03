#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
if a > b:
    print('O primeiro número digitado {} é maior que o segundo número digitado {}'.format(a. b))
elif a < b:
    print('O segundo número digitado {} é maior que o primeiro número digitado {}'.format(b, a))
else:
    print('Os dois núreros {} e {} são iguais'.format(a, b))

print('Obrigado!')
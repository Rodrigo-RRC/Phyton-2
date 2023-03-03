#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))

print('Escolha abaixo a base que você quer a conversão.')

print("""
[1]Opção: Converter para Base Binária
[2]Opção: Converter para Base Octal
[3]Opção: Converter para Base Hexadecimal""")

opção = int(input('Digite aqui a sua opção: '))


if opção == 1:
    print("{} convertido para BINÁRIO fica {}".format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL fica {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL fica {}'.format(num, hex(num)[2:]))
else:
    print('Opçâo inválida. Tente novamente!')
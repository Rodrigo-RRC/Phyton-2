#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('LOJAS CARVALHO'))
valorDosProdutos = float(input('Valor dos Produtos na Prateleira: R$ '))
print('Escolha a Opção de Pagamento:')
print("""FORMAS DE PAGAMENTO
[1] À vista (Dinheiro/Cheque) - Desconto de 10%, 
[2] À vista no Cartão - Desconto de 5%, 
[3] 2 x no Cartão - Preço Normal,
[4] 3 ou mais x no Cartão - Juros de  20%""")
opção = int(input('Digite a opção: '))

if opção == 1:
    total = valorDosProdutos * 0.90
    print('O valor {:.2f} passa a ser: R$ {:.2f}'.format(valorDosProdutos, total))
elif opção == 2:
    total = valorDosProdutos * 0.95
    print('O valor {:.2f} passa a ser: R$ {:.2f}'.format(valorDosProdutos, total))
elif opção == 3:
    total = valorDosProdutos
    parcela = total / 2
    print('O valor a ser pago será R$ {:.2f}, e será dividido em 2 parcelas iguais no cartão de: R$ {:.2f}'.format(valorDosProdutos,parcela))
elif opção == 4:
    total = valorDosProdutos * 1.20
    print('O valor total será de R$ {:.2f}'.format(total))
    print('O máximo de parcelas será de 6')
    totalDeParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalDeParcelas
    print('Sua compra será parcelado em {} vezes e você pagará R$ {:.2f} por cada parcela'.format(totalDeParcelas, parcela))
else:
    print('Opção INVÀLIDA. Refaça o Processo.')

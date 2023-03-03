valorCasa = float(input('Qual o valor de casa que pretendes financiar?R$ '))
salario = float(input('Qual é o valor de seu salário bruto?R$'))
tempo = float(input('Em quanto anos quer realizar o financiamento?'))
tempoMeses = tempo *12
prestacao = valorCasa / tempoMeses
if prestacao > 0.30 * salario:
    print('O banco não poderá financiar seu imóvel pois sua prestação será de R$ {:.2f} e, portanto, excede 30% do seu salário que é {:.2f}'.format(prestacao, 0.30 * salario))
else:
    print('Seu financiamento está aprovado e você irá pagar R$ {:.3f} de prestação'.format(prestacao))

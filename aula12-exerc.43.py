#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
import math

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

# IMC = Peso(KG) / (Altura)² [METRO]

print('-=-'*20)
print('           IMC - ÍNDICE DE MASSA CORPORAL')
print('-=-'*20)

peso = float(input('Digite sua massa em KG: '))
altura = float(input('Agora digite sua altura em metros: '))
imc = (peso) / math.pow(altura, 2)

if imc <  18.5:
    print('Você está \033[33mABAIXO DO SEU PESO\033[m, pois seu IMC é: {:.1f} KG/m²'.format(imc))
elif 18.5 <= imc <  25:
    print('Você está com \033[33mPESO IDEAL\033[m, pois seu IMC é: {:.1f} KG/m²'.format(imc))
elif 25 <= imc <  30:
    print('Você está com \033[33mSOBREPESO\033[m, pois seu IMC é: {:.1f} KG/m²'.format(imc))
elif 30 <= imc <  40:
    print('Você está com \033[33mOBESIDADE\033[m, pois seu IMC é: {:.1f} KG/m²'.format(imc))
elif imc >=40:
    print('Você está com \033[33mOBESIDADE MÓRBITA\033[m, pois seu IMC é: {:.1f} KG/m²'.format(imc))

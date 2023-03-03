#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

a = float(input('Digite o primeiro segmento de reta: '))
b = float(input('Digite o segundo segmento de reta: '))
c = float(input('Digite o terceiro segmento de reta: '))

if a < b + c and b < a + c and c < a + b and a == b == c:
    print('Os segmentos PODEM formar um triângulo do tipo \033[35mEQUILÁTERO!\033[m')
elif a < b + c and b < a + c and c < a + b and a == b or a == c or b == c:
    print('Os segmentos PODEM formar um triângulo do tipo \033[35mISÓSCELES!\033[m')
elif a < b + c and b < a + b and c < a + b and a != b and a != c and b != c:
    print('Os segmentos PODEM formar um triângulo do tipo \033[35mESCALENO!\033[m')

else:
    print('Os segmentos de reta \033[35mNÃO PODEM FORMAR UM TRIÃNGULO\033[m. \033[36mESCOLHA OUTROS VALORES\033[m')

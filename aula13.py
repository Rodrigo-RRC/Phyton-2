#for d in range (6,-1,-2):
   # print(d) #Dentro do for
#print('fim')

#n = int(input('Digite um número:'))
#for c in range(0, n+1):
   # print(c)
#print("Fim")

#inicioContagem = int(input('Digite o número de início da contagem: '))
#fimContagem = int(input('Digite o fim da contagem: '))
#passoContagem = int(input('Qual a variação: '))
#for c in range(inicioContagem, fimContagem + 1, passoContagem):
   # print(c)
#print('Fim')

soma = 0
for c in range(0, 4):
    n = int(input('Didite um número: '))
    soma+=n
print('A soma dos números digitados é: {}'.format(soma))
quadrado = pow(soma, 2)
print('E sua potência elevado ao expoente 2 é: {}'.format(quadrado))
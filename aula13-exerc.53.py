
frase = str(input('Escreva uma frase ao lado => ')).strip().upper()#strip - para tirar os espaços antes e depois da frase
                                                                   #upper - para passar as letras para maiúscula
palavras = frase.split() # split serve para separar as palavras da frase
#junto = ''.join(palavras) # join - serve para tirar os espaços internos da frase ou juntar e acrescentar um simbolo, por exemplo
junto = ''.join(palavras)
inverso = junto[::-1] #''' #primeiro: = Começa no início da frase (Posição zero); segundo: = Fim da frase (posição final) e -1 + contagem do fim para o início de 1 em 1'''
#print('A frase digitada foi: {}'.format(frase))
#print('A frase digitada foi: {}'.format(palavras))
#print('A frase digitada foi: {}'.format(junto))
'''for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]'''
if inverso == junto:
    print('O inverso da {} é {}.'.format(junto, inverso))
    print("Logo temos um Palíndromo!")
else:
    print('A frase não é um Palíndromo')
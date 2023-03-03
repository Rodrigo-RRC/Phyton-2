nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Rodrigo':
    print('Seu nome é um espetáculo!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Nomezinho bem popular hein!!!')
elif nome in ('Ana Julia Beatriz'):
    print('Belo nome!')
else:
    print('Nome bem comum hein!!!')
print('Tenha um excelente dia {}"'.format(nome))
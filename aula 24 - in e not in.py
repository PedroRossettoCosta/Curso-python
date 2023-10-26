nome = input('Escreva o seu nome: ')
encontrar = input('escreva o q está buscando: ')

if encontrar in nome:
    print(f'{encontrar} está dentro de {nome}')
    
else:
    print(f'{encontrar} não está dentro de {nome}')
"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade form digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios"

"""

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')

if nome and idade: 
    print(f'Seu nome é {nome}')
    print('\nSeu nome invertido é',nome[::-1])
   
    if ' ' in nome:
        print('\nTem espaços no seu nome')

    else:
        print('\nSeu nome não contem espaços')
    print('\nSeu nome tem',len(nome),'letras')
    print('\nA primeira letra do seu nome é',nome[0])
    tamanho = len(nome) - 1
    print('\nA ultima letra do seu nome é',nome[tamanho])

else:
    print('\nDesculpe, você deixou campos vazios')

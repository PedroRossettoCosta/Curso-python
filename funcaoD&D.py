import random

dados = ""
def rolador(dados):

    lista_numeros = []

    x = dados.split("d")
    
    quantidade = int(x[0])
    tamanho = int(x[1])

    for i in range(quantidade):
        numero = random.randint(1,tamanho)
        lista_numeros.append(numero)

    
    return(lista_numeros)

    

print(rolador("2d8"))
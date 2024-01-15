#Para decidirmos o valor de um status no d&d, rolamos 4d6 e descartamos o menor valor o somar o resto.
#depois disso, repetimos os processo mais 5 vezes até termos os 6 status necessarios.
#faça uma função que retorne uma lista com os 6 status de um personagem

import random


def rolador_status(dados):

    lista_status = []
    

    x = dados.split("d")
    
    quantidade = int(x[0])
    tamanho = int(x[1])
    
    for i in range(6):
        lista_numeros = []
        for i in range(quantidade):
            numero = random.randint(1,tamanho)
            lista_numeros.append(numero)


        lista_numeros.sort()
        lista_numeros.remove(lista_numeros[0])
        status = sum(lista_numeros)

        lista_status.append(status)
    print(lista_numeros)
    return(lista_status)

print(rolador_status("4d6"))

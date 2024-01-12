import random
import time

def reqMinimo(requerimento):
    
    lista_status = []
    quantidade_roladas = 0

    while True:
        lista_status = []
        for i in range(6):
            lista_numeros = []
            for j in range(4):
                numero = random.randint(1,6)
                lista_numeros.append(numero)
                
            lista_numeros.sort()
            lista_numeros.remove(lista_numeros[0])
            status = sum(lista_numeros)

            lista_status.append(status)
    
        statusTotal = sum(lista_status)

        quantidade_roladas += 1

        if statusTotal >= requerimento:
            tupla = (quantidade_roladas, lista_status)
            return(tupla)
        
def mediaRoladaParaValor(requerimento,roladas):
    tempo = 0
    listaRoladas = []
    inicio = time.time()
    for i in range(roladas):
        print(len(listaRoladas))
        tupla = reqMinimo(requerimento)
        listaRoladas.append(tupla[0])
    fim = time.time()

    tempo = (fim - inicio)
    totalListaRoladas = sum(listaRoladas)
    print(f"demorou: {tempo} para rodar o programa")
    mediaRoladas = totalListaRoladas/roladas    

    print(mediaRoladas)
    
        

print(mediaRoladaParaValor(90,10000))

import time
import random
# randint only for integers, uniform for floats aswell

def simuladorDownload(tamanho):
    
    downloadAtual = 0 
    tamanho = tamanho * 1024
    downloadCompleto = tamanho

    

    while downloadAtual < downloadCompleto: 
        velocidade = random.uniform(100,500)
        print(f"{velocidade}Kbs")
        downloadAtual += velocidade
        print(downloadAtual)
        porcentagem = (round(((downloadAtual/tamanho)*100),2))
        
        print(f"{porcentagem}%")
        print("["+("#"*(int(10*(downloadAtual/ downloadCompleto)))).ljust(10)+"]")

        if downloadAtual >= downloadCompleto:
            print("O download esta completo!")

        time.sleep(1)

simuladorDownload(15)
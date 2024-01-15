escolha = input("Escolha 1 para ver MEDIA, 2 para ver oq vc precisa tirar na AP2, 3 para fazer a media do periodo inteiro:  ")

def media():
    ap1 = float(input("Ap1 :  ").replace("," ,"."))
    ac = float(input("ac : ").replace("," ,"."))
    ap2 = float(input("ap2 :  ").replace("," ,"."))
    med = (ap1 *0.4) + (ac * 0.2) + (ap2*0.4)
    print(f"a sua média é {med}")

    if(med >= 7):
        print("Voce passou está materia!")
    else:
        print("Voce não está passando está materia")

    

def falta():
    ap1 = float(input("Ap1 :  "))
    ac = float(input("ac : "))
    ag = ap1*0.4 + ac*0.2
    resta = 7 - ag
    resta = resta / 0.4
    print(f"Vc precisar tirar {resta} na AP2 para passar!")

def media_periodo():
    print("entrou")
    mTotal = 0
    for i in range(1, 6):
        ap1 = float(input("Ap1 :  ").replace(",", "."))
        ac = float(input("ac : ").replace(",", "."))
        ap2 = float(input("ap2 :  ").replace(",", "."))
        med = (ap1 *0.4) + (ac * 0.2) + (ap2*0.4)
        print(f'{med}')
        if(med >= 7):
            print("Voce passou está materia!")
        else:
            print("Voce não está passando está materia")
        mTotal = mTotal + med
        print(f"notas somadas até agora: {mTotal}")

    mTotal = mTotal / 5
    print(f"A sua media no periodo é {mTotal}")
    

if(escolha == "1"):
    media()
elif(escolha == "2"):
    falta()
elif(escolha == "3"):
    media_periodo()
else:
    print("Isto não eh uma opção!!!")

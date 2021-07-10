def Troco(pre,pag):
    troco = round(pag-pre,2)
    
    qtdNts = [0,"R$100.00",0,"R$50.00",0,"R$20.00",0,"R$10.00",0,"R$5.00",0,"R$2.00",0,"R$1.00",0,"R$0.50",0,"R$0.25",0,"R$0.10",0,"R$0.05",0,"R$0.01"]

    print("Troco: R$"+(str(troco)))
    print("==============================================")

    while(True):
        if((troco-100) >= 0):
            troco = troco-100
            qtdNts[0] += 1
        elif((troco-50) >= 0):
            troco = troco-50
            qtdNts[2] += 1
        elif((troco-20) >= 0):
            troco = troco-20
            qtdNts[4] += 1
        elif((troco-10) >= 0):
            troco = troco-10
            qtdNts[6] += 1
        elif((troco-5) >= 0):
            troco = troco-5
            qtdNts[8] += 1
        elif((troco-2) >= 0):
            troco = troco-2
            qtdNts[10] += 1
        elif((troco-1) >= 0):
            troco = troco-1
            qtdNts[12] += 1
        elif((troco-0.5) >= 0):
            troco = troco-0.5
            qtdNts[14] += 1
        elif((troco-0.25) >= 0):
            troco = troco-0.25
            qtdNts[16] += 1
        elif((troco-0.1) >= 0):
            troco = troco-0.1
            qtdNts[18] += 1
        elif((troco-0.05) >= 0):
            troco = troco-0.05
            qtdNts[20] += 1
        elif((troco-0.01) >= 0):
            troco = troco-0.01
            qtdNts[22] += 1
        else:
            break
        
    for x in range(0,len(qtdNts),2):
        if(qtdNts[x]>0 and x < 12):
            print(qtdNts[x],"Nota(s) de",qtdNts[x+1])
        elif(qtdNts[x]>0 and x >= 12):
            print(qtdNts[x],"Moeda(s) de",qtdNts[x+1])
    
#Loop do programa

while(True):
    try:
        print("==============================================")
        Preco = float(input("Informe o preço do produto:"))
        while(True):
            try:
                Pago = float(input("Informe o valor que foi pago: "))
                if(Preco>Pago):
                    print("O valor pago não cobre o custo do produto.")
                else:
                    break
            except:
                print("==============================================")
                print("Comando inválido, tente novamente.")
                print("==============================================")

        print("==============================================")
        Troco(Preco,Pago)
        print("==============================================")
        break
    except:
        print("==============================================")
        print("Comando inválido, tente novamente.")
        print("==============================================")

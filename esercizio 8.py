import random

def main():
    pass

opzioni = ["SASSO", "CARTA", "FORBICE"]

while 1 > 0:
    print("digita \"quit\" per uscire")

    mossa1 = input("Giocatore 1, Inserisci la tua mossa: ")
    mossa1 = mossa1.upper()
    if mossa1 == "QUIT":
        break
    while mossa1 not in opzioni:
        mossa1 = input("Opzione non disponibile!\nGiocatore 1, Inserisci la tua mossa: ")
        mossa1 = mossa1.upper()

    #mossa2 = input("Giocatore 2, Inserisci la tua mossa: ")
    #mossa2 = mossa2.upper()
    #if mossa2 == "QUIT":
    #    break
    #while mossa1 not in opzioni:
    #    mossa2 = input("Opzione non disponibile!\nGiocatore 2, Inserisci la tua mossa: ")
    #    mossa2 = mossa2.upper()
    mossa2 = random.choice(opzioni)
    mossa2 = mossa2.lower().capitalize()
    print("CPU dice " + mossa2)

    mossa2 = mossa2.upper()
    if(mossa1 == "SASSO" and mossa2 == "FORBICE") or (mossa1 == "CARTA" and mossa2 == "SASSO") or (mossa1 == "FORBICE" and mossa2 == "CARTA"):
        #print("Giocatore 1 vince!")
        print("Hai vinto!")
    else:
        if mossa1 == mossa2:
            print("Parità")
        else:
            #print("Giocatore 2 vince!")
            print("CPU vince!")

if __name__ == "__main__":
    main()
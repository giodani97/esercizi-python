def reverser(stringI):
    #converto la stringa in una lista splittandola usando lo spazio come splitter
    stringSplitted = stringI.split(" ")
    #faccio un reverse della lista
    stringSplitted.reverse()
    #creo la stringa result facendo un join degli elementi della lista(parole) inframezzate da spazi
    result = " ".join(stringSplitted)
    return result

inputString = input("Inserisci la stringa da invertire: ")

print(reverser(inputString))
def main():
    pass

numero = int(input("Inserisci un numero: "))
check = int(input("Inserisci per cosa dividerlo: "))
if (numero % check) == 0:
    if(numero % 4) == 0:
        print("Il risultato è un numero pari ed è un multiplo di 4!")
    else:
        print("Il risultato è un numero pari!")
else:
    print("Il risultato è un numero dispari!")

if __name__ == "__main__":
    main()





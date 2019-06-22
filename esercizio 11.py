def main():
    pass
prime = False
numero = int(input("Inserisci il numero da verificare: "))
for i in range(2, numero):
    if numero % i == 0 and i != numero:
        prime = True
        print("Il numero " + str(numero) + " non è primo")
        exit()
print("Il numero " + str(numero) + " è primo")

if __name__ == "__main__":
    main()
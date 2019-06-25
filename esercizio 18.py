import random

if __name__ == "__main__":
    toGuess = random.randint(999,9999)
    print(toGuess)
    print("Benvenuto al gioco mucche e tori!")
    counter = 0
    while True:
        cow = 0
        bull = 0
        guess = int(input("Inserisci un numero: "))
        while guess < 1000 or guess > 9999:
            print("Il numero deve essere di 4 cifre!")
            guess = int(input("Inserisci un numero: "))
        counter += 1
        for digit in range(0, len(str(toGuess))):
            if str(toGuess)[digit] == str(guess)[digit]:
                cow += 1
            else:
                for digit2 in range(0, len(str(toGuess))):
                    if str(toGuess)[digit2] == str(guess)[digit]:
                        bull += 1
        print(str(cow) + (" mucca, " if cow == 1 else " mucche, ") + str(bull) + (" toro." if bull == 1 else " tori."))
        if cow == len(str(toGuess)):
            print("Hai vinto! Hai indovinato in " + str(counter) + ( " tentativo!" if counter == 1 else " tentativi!"))
            exit()

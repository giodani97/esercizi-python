def main():
    pass

import random

while True:
    scelta = input("Indovina il numero (tra uno e dieci) oppure digita \"quit\" per uscire: ")
    if scelta == "quit":
        break
    generated = random.randint(1, 10)
    if int(scelta) == generated:
        print("Hai indovinato!")
    else:
        if int(scelta) > generated:
            print("troppo alto!")
        else:
            print("troppo basso!")
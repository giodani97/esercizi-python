from datetime import date
def main():
    pass

nome = input("Come ti chiami? ")
print("Ti chiami " + nome)

today = date.today()
eta = int(input("Quanti anni hai? "))
print("Hai " + str(eta) + " anni")
print("Compierai 100 anni l'anno: " + str(int(today.strftime("%Y")) - eta + 100))

if __name__ == "__main__":
    main()
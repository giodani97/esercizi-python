def main():
    pass

original = input("Inserisci la stringa da verificare: ")
reversed = ""

for i in original:
    reversed = i + reversed

if original == reversed:
    print("La stringa è palindroma")
else:
    print("La stringa non è palindroma")

if __name__ == "__main__":
    main()
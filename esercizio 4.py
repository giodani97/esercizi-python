def main():
    pass

daDividere = int(input("Inserisci il numero di cui trovare i divisori: "))

for num in range(2, daDividere):
    if (daDividere % num) == 0:
        print(num)

if __name__ == "__main__":
    main()
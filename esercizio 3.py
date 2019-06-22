def main():
    pass

comparator = int(input("Inserisci il comparatore: "))
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []

for num in list:
    if num < comparator:
        newlist.append(num)

print(newlist)

if __name__ == "__main__":
    main()
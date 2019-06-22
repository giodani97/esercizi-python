def main():
    pass

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
finalList = [element for element in a if element % 2 == 0]

print(finalList)

if __name__ == "__main__":
    main()
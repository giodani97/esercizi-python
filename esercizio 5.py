def main():
    pass

import random

finalList = []
listA = []
listB = []

for i in range(50):
    listA.append(random.randint(0, 100))
    listB.append(random.randint(0, 100))

print("Lista A: " + str(listA))
print("Lista B: " + str(listB))

for elementA in listA:
    if elementA in listB:
        if elementA not in finalList:
            finalList.append(elementA)
#for elementA in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]:
#    if elementA in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
#        if elementA not in finalList:
#            finalList.append(elementA)
finalList.sort()
print("Le liste hanno in comune: " + str(finalList))

if __name__ == "__main__":
    main()
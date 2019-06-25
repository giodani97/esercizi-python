import random

def useList(listA):
    listB = []
    for i in range(0, len(listA)):
        if listA[i] not in listB:
            listB.append(listA[i])
    return listB

def useSet(listA):
    return set(listA)

listI = [random.randint(0,15) for i in range(0,40)]
print(listI)
usingList = useList(listI)
usingSet = useSet(listI)
print(usingList)
print(usingSet)

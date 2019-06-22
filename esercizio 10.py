def main():
    pass

import random

listA = random.sample(range(1000), 40)
listB = random.sample(range(1000), 45)
listFinal = [i for i in set(listA) if i in set(listB)]
print("Lista A: " + str(listA))
print("Lista B: " + str(listB))
print("Elementi in comune: " + str(listFinal))
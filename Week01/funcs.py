import random
def generateRandomArray():
    n=30000
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 100000))
    return arr
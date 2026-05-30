import random


def max(randlst):
    tempmax = 0
    nummax = 0
    for i in range(len(randlst) - 1):
        # for j in range (len(randlst)):
        if randlst[i] > tempmax:
            tempmax = randlst[i]
            # else:
            #     nummax = randlst[i+1]
    return tempmax


def main():
    randlst = []
    for i in range(0, 100):
        randlst.append(int(random.random() * 1001))
        # print (randlst, end=' ')
    print(randlst)
    print(max(randlst))


main()

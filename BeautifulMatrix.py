i1 = input()
i2 = input()
i3 = input()
i4 = input()
i5 = input()

l1 = i1.split()
l2 = i2.split()
l3 = i3.split()
l4 = i4.split()
l5 = i5.split()

ml = [l1, l2, l3, l4, l5]

def findone(ml):
    for i in range(len(ml)):
        for j in range(len(ml[i])):
            if ml[i][j] == '1':
                return makebeauti(i, j)

def makebeauti(i, j):
    return abs(i - 2) + abs(j - 2)

steps = findone(ml)
print(steps)

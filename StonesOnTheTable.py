x = int(input())
y = input()
l = list(y)
count = 0
i = 0
while i < len(l) - 1:
    if l[i] == l[i + 1]:
        l.pop(i + 1)
        count += 1
    else:
        i+=1
print(count)

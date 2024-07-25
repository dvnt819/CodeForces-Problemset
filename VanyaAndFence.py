x=input().split()
y=input().split()
width=0
for i in range(int(x[0])):
    if int(y[i])>int(x[1]):
        width+=2
    else:
        width+=1
print(width)

x=int(input())
max=0
current=0
for i in range(x):
    l=input().split()
    current=current+int(l[1])-int(l[0])
    if current>max:
        max=current
print(max)

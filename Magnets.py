x=int(input())
count=1
l=list()
for _ in range(x):
    l.append(input())
i=0
while i<x-1:
    if l[i] != l[i+1]:
        count+=1
    i+=1
print(count)

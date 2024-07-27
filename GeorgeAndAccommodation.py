x=int(input())
count=0
for _ in range(x):
    l=input().split()
    if int(l[1])-int(l[0])>1:
        count+=1
print(count)

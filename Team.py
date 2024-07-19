x=int(input())
ans=0
while x>0:
    c=input()
    l=c.split()
    s=0
    for i in l:
        if i=='1':
            s+=1
    if s>=2:
        ans+=1
    x-=1
print(ans)

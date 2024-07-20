z=input()
x=z.split()
p=int(x[1])-1
ans=0
c=input()
l=c.split()
for i in l:
    if int(i)>=int(l[p]):
        if int(i)!=0:
            ans+=1
print(ans)

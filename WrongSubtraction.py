x=input().split()
n=int(x[0])
t=int(x[1])
while t>0:
    if n%10==0:
        n=n/10
    else:
        n=n-1
    t-=1
print(int(n))

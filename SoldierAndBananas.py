x = input().split()
k=int(x[0])
n=int(x[1])
w=int(x[2])
amount=0
while w>0:
    amount=amount+k*w
    w-=1
if (amount-n)<0:
    print(0)
else:
    print(amount-n)

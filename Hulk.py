n=int(input())
feeling="I hate"
for i in range(2,n+1):
    if i%2==0:
        feeling+=" that I love"
    else:
        feeling+=" that I hate"
feeling+=" it"
print(feeling)

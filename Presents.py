x=int(input())
y=input()
l = list(map(int, y.split()))
ans=[0]*x
for i in range(x):
    ans[l[i]-1]= i+1

for i in ans:
    print(i)

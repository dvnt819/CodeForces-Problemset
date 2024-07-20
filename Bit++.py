x=int(input())
ans=0
while x>0:
    c=input()
    if c=="X++" or c=="++X":
        ans+=1
    if c=="X--" or c=="--X":
        ans-=1
    x-=1
print(ans)

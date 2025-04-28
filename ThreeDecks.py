n=int(input())
for _ in range(n):
    x,y,z=map(int,input().split())   
    if((x+y+z)%3 == 0 and (y-x)<=(z-y)):
        print("YES")
    else:
        print("NO")

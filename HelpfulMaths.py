s=input()
l=s.split("+")
l.sort()

for i in range (len(l)):
    print(l[i],end="")
    if i!=(len(l)-1):
        print("+",end="")
    

x=input()
y=list(input())
check=0
for i in y:
    if i=="A":
        check+=1
    else:
        check-=1
if check>0:
    print("Anton")
elif check<0:
    print("Danik")
else:
    print("Friendship")

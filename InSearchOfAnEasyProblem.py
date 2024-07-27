x=int(input())
y=input().split()
check=0
for i in y:
    if i=="1":
        check=1
        break
if check==1:
    print("HARD")
else:
    print("EASY")

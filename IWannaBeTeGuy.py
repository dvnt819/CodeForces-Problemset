x=int(input())
y=input().split()
z=input().split()
y.pop(0)
z.pop(0)
check=True
for i in range(1,x+1):
    if str(i) in y or str(i) in z:
        continue
    else:
        check=False
if check:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

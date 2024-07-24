x=input()
check=0
for i in x:
    if i==i.upper():
        check+=1
    else:
        check-=1
if check>0:
    print(x.upper())
else:
    print(x.lower())

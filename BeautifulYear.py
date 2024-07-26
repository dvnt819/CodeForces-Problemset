x=int(input())
while True:
    y=set(str(x+1))
    if len(y)<4:
        x+=1
    else:
        break
print(x+1)

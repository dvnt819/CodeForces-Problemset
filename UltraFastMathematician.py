x=input()
y=input()
maxlen=max(len(x),len(y))
x=int(x,2)
y=int(y,2)
result=x^y
result=bin(result)[2:]
print(result.zfill(maxlen))

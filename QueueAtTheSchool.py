x=input().split()
y=list(input())
for _ in range(int(x[1])):
    i=0
    while i < int(x[0])-1:
        if y[i]=="B" and y[i+1]=="G":
            y[i]="G"
            y[i+1]="B"
            i=i+1
        i=i+1
print("".join(y))

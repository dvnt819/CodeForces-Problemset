s=int(input())
while s>0:
    w=input()
    if len(w)>10:
        print(f"{w[:1]}{len(w)-2}{w[-1]}")
    else:
        print(w)
    s-=1

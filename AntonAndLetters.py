x=set(input())
if "," in x:
    x.remove(",")
if " " in x:
    x.remove(" ")
x.remove("{")
x.remove("}")
print(len(x))

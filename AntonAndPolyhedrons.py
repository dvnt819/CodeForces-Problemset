x=int(input())
count=0
for _ in range(x):
    y=input()
    if y=="Tetrahedron":
        count=count+4
    if y=="Cube":
        count+=6
    if y=="Octahedron":
        count+=8
    if y=="Dodecahedron":
        count+=12
    if y=="Icosahedron":
        count+=20
print(count)

n=int(input())
count=0
for i in range(n):
    x=input()
    if(x=="Tetrahedron"):
        count+=4
    if(x=="Cube"):
        count+=6
    if(x=="Octahedron"):
        count+=8
    if(x=="Dodecahedron"):
        count+=12
    if(x=="Icosahedron"):
        count+=20
print(count)
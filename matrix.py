n=int(input())
m=int(input())
a=[]
b=[]
c=[]
d=[]
for j in range(m):
    for i in range(n):
        x=int(input())
        a.append(x)
    b.append(a)
    a=[]

for j in range(m):
    for i in range(n):
        x=int(input())
        a.append(x)
    c.append(a)
    a=[]

for j in range(m):
    for i in range(n):
        print(b[j][i]+c[j][i])

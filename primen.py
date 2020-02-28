flag=0
print(1)
print(2)
for i in range(3,100+1):
    for j in range(2,i):
        if(int(i%j)==0):
            flag=0
            break
        else:
            flag=1
    if(flag==1):
        print(i)


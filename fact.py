n=int(input())

fact=1

if(n<0):
    print("no fact for negative number")
elif(n==0):
    print("no fact for zero")
else:
    for i in range(1,n+1):
        fact= fact*i
    print("factorial is ",fact)

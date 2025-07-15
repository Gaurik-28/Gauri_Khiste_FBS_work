start=int(input("enter the number"))
stop=int(input("enter the number"))
for x in range(start,stop+1):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x)        
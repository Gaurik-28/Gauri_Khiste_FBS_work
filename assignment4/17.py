#print prime no from 1 to 100
for x in range(2,101):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x)   

    
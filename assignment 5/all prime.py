
for x in range(1,101):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x)        
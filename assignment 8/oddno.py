def odd():
    sum=0
    n=int(input("enter the number"))
    for i in range(1,n+1):
        if(i%2!=0):
            sum=sum+i     
    print(sum)         
odd()            

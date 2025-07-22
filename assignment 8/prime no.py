def prime():
    sum=0
    
    for x in range(2,n+1):
        for i in range(2,x):
            if(x%i==0):
                break
        else:
            sum=sum+x 
            print(sum)    
          
n=int(input("enter the number"))      
prime()            

 
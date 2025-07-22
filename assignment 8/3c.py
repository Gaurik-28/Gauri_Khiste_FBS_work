def square(n):
    sum=0
    for i in range(1,n+1):
        sum=(i ** i)+sum
    return sum
    
n=int(input("enter the number"))
result=square(n)    
print(result)
    


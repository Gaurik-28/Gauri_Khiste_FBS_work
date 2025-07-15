# WAP to check if a given number is prime number or not.
num=int(input("enter the number"))
for i in range(2,num):
    if(num%i==0):
        print("it is not prime number")
        break
else:
    print("it is prime number")        

# WAP to print all odd numbers until n.
start=int(input("enter the number"))
stop=int(input("enter the number"))
for i in range(start,stop):
    
    if(i%2!=0):
        print(i)